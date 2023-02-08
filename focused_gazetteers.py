# -*- coding: utf-8 -*-

import time

import sqlite3
import string
import re
import pandas
import os

from tqdm import tqdm
from shapely import wkt
from shapely.geometry import Point
from nltk.tokenize import sent_tokenize
from nltk.util import ngrams
from pandas import ExcelWriter
from pandas import ExcelFile


stopwords = [
    'A', 'À', 'Agora', 'Ainda', 'Além', 'Alguém', 'Algum', 'Alguma', 'Algumas',
    'Alguns', 'Ampla', 'Amplas', 'Amplo', 'Amplos', 'Ante', 'Antes', 'Ao',
    'Aos', 'Após', 'Aquelas', 'Aquele', 'Aqueles', 'Aquilo', 'As', 'Às', 'Até',
    'Através', 'Bem', 'Bom', 'Cada', 'Coisa', 'Coisas', 'Com', 'Como',
    'Contra', 'Contudo', 'Da', 'Daquele', 'Daqueles', 'Das', 'De', 'Dela',
    'Delas', 'Dele', 'Deles', 'Depois', 'Dessa', 'Dessas', 'Desse', 'Desses',
    'Desta', 'Destas', 'Deste', 'Destes', 'Disso', 'Disto', 'Dito', 'Do',
    'Dos', 'E', 'É', 'Ela', 'Elas', 'Ele', 'Eles', 'Em', 'Enquanto', 'Entre',
    'Era', 'Eram', 'Éramos', 'Essa', 'Essas', 'Esse', 'Esses', 'Esta', 'Está',
    'Estão', 'Este', 'Estes', 'Estou', 'Eu', 'For', 'Há', 'Isso', 'Isto', 'Já',
    'La', 'Lá', 'Lhe', 'Lhes', 'Lo', 'Mais', 'Mau', 'Mal', 'Mas', 'Me',
    'Mesma', 'Mesmas', 'Mesmo', 'Mesmos', 'Meu', 'Meus', 'Minha', 'Minhas',
    'Muita', 'Muitas', 'Muito', 'Muitos', 'Na', 'Não', 'Nas', 'Nele', 'Neles',
    'Nesse', 'Nesses', 'Neste', 'Nestes', 'Nem', 'Nenhum', 'Nessa', 'Nessas',
    'Nesta', 'Nestas', 'Ninguém', 'No', 'Nos', 'Nós', 'Nossa', 'Nossas',
    'Nosso', 'Nossos', 'Num', 'Numa', 'Nunca', 'O', 'Os', 'Ou', 'Onde',
    'Outra', 'Outras', 'Outro', 'Outros', 'Para', 'Pela', 'Pelas', 'Pelo',
    'Pelos', 'Pequena', 'Pequenas', 'Pequeno', 'Pequenos', 'Per', 'Perante',
    'Pois', 'Por', 'Porém', 'Porque', 'Posso', 'Pouca', 'Poucas', 'Pouco',
    'Poucos', 'Primeiro', 'Primeiros', 'Própria', 'Próprias', 'Próprio',
    'Próprios', 'Pude', 'Quais', 'Qual', 'Quando', 'Quanto', 'Quantos', 'Que',
    'Quem', 'São', 'Se', 'Seja', 'Sejam', 'Sem', 'Sempre', 'Seu', 'Seus',
    'Si', 'Sido', 'Só', 'Sob', 'Sobre', 'Somos', 'Sou', 'Sua', 'Suas',
    'Talvez', 'Também', 'Tampouco', 'Te', 'Tém', 'Tem', 'Têm', 'Teu', 'Teus',
    'Teve', 'Ti', 'Toda', 'Todas', 'Todavia', 'Todo', 'Todos', 'Tu', 'Tua',
    'Tuas', 'Tudo', 'Última', 'Últimas', 'Último', 'Últimos', 'Um', 'Uai',
    'Uma', 'Umas', 'Uns', 'Vendo', 'Ver', 'Vez', 'Vindo', 'Vir', 'Você',
    'Vocês', 'Vos', 'Vós']


# Extract the namefile
def get_filename(url):
    url = url.strip()
    point = url.rfind('.')
    slash = url.rfind('/')
    url = url[slash+1:point]
    return url


# Aux funcion used by find_all
def find_all_aux(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


# Aux function to order the list_c in clean_candidate function
def order_list_c(l):
    return l[1]


# Aux funcion used by clean_candidates
def find_all(a_str, sub):
    l = []
    l = l + list(find_all_aux(a_str, sub))
    return l


# Aux function to remove some characters
def clean_string(txt):
    return re.sub(u'[^a-zA-Z0-9àÀáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', txt)


# Remove false candidates
def clean_candidates(text, candidates):

    only_names = []
    for item in candidates:
        if item[0] not in only_names:
            only_names.append(item[0])

    list_c = []
    for c in list(dict.fromkeys(only_names)):
        # Position's list of a word c in the text
        t = (c, find_all(text, c))
        list_c.append(t)

    for c in list_c:
        for n in list_c:
            if (n[0] != c[0] and n[0] in c[0]):
                for pos_c in c[1]:
                    for pos_n in n[1]:
                        if pos_n >= pos_c and pos_n <= (pos_c + len(c[0])):
                            n[1].remove(pos_n)

    list_c.sort(key=order_list_c)

    resp = []
    for c in list_c:
        if c[1] != []:
            resp.append(c[0])

    final_list = []
    for item in candidates:
        if item[0] in (list(dict.fromkeys(resp))):
            final_list.append(item)

    return final_list


# Make all n-gram (size n) of a text
def make_ngrams(text, n):

    resp_list = []

    # Break the text into individual tokens
    tokenized = text.split()

    # Get the lowest value to create ngram
    limit = min(n, len(tokenized))

    ngram_list = list(ngrams(tokenized, limit))
    tail_ngram = list(list(ngrams(tokenized, limit-1))[-1])

    while (ngram_list):
        s = clean_string(' '.join(ngram_list[0]).strip(string.punctuation))
        if len(s) < 1:
            s = 'z'
        if (s[0].isupper()):
            resp_list.append(s)
            x = list(ngram_list.pop(0))
            while (x):
                x.pop(-1)
                s = clean_string(' '.join(x).strip(string.punctuation))
                if len(s) > 0:
                    resp_list.append(s)
        else:
            ngram_list.pop(0)

    # Tail ngram
    while (len(tail_ngram) > 0):
        tail_ngram.pop(0)
        s = clean_string(' '.join(tail_ngram).strip(string.punctuation))
        if (s and s[0].isupper()):
            resp_list.append(s)
            aux = tail_ngram.copy()
            while (aux):
                aux.pop(-1)
                s = clean_string(' '.join(aux).strip(string.punctuation))
                if (len(s) > 0):
                    resp_list.append(s)

    return resp_list


# Creates a Multipolygon/Polygon using the wkt file
def create_polygons(wkt_file):
    folder_path = '/home/bruno/workspace/Doutorado/wkt_polygons/'
    extension_file = '.wkt'
    with open(folder_path + wkt_file + extension_file, 'r') as file:
        geom = wkt.loads(file.readline())
    file.close()

    return geom


# Geoparsing the geonames database
def geoparsing_geonames(text):
    candidates = []
    # Breaking the news on a multiple lines
    list_lines = sent_tokenize(text)

    complete_path = '/home/bruno/workspace/Doutorado/Resultados/'
    conn = sqlite3.connect(complete_path + 'geonames.db')
    cursor = conn.cursor()

    # For each line, get all toponyms' candidates
    for line in list_lines:
        line_ngram = make_ngrams(line, 5)
        for ngram in line_ngram:
            if len(ngram) > 1 and (ngram not in stopwords):
                cursor.execute("SELECT * FROM geonames WHERE name=?", (ngram,))
                results = cursor.fetchall()
                if results:
                    candidates += list((set(results) - set(candidates)))
    conn.close()

    toponyms_list = []
    cleaned_candidates = clean_candidates(text, candidates)

    for item in cleaned_candidates:
        temp_dict = {
            "name": item[0],
            "points": []
        }

        if temp_dict not in toponyms_list:
            toponyms_list.append(temp_dict)

    for item in cleaned_candidates:
        for t in toponyms_list:
            if item[0] == t["name"]:
                point = "POINT (" + str(item[2]) + ' ' + str(item[1]) + ")"
                t["points"].append(point)
                t["total_points"] = len(t["points"])

    return toponyms_list


# Filter result using API_GIS
def filter_toponyms(tp_list, multipolygon):

    # Runs over the dict list result
    for item_dict in tp_list:

        variable_list = [
            p for p in item_dict["points"] if wkt.loads(p).within(multipolygon)
            ]

        item_dict["points"] = variable_list
        item_dict["total_points"] = len(item_dict["points"])

    return [item for item in tp_list if item["total_points"] > 0]

    
# Save result in xlsx file
def save_xlsx(namefile, tp_list1, tp_list2, tp_list3, tp_list4, tp_list5):

    final_result = pandas.DataFrame({
        'Global': pandas.Series([t["name"] for t in tp_list1], dtype="object"),
        'Global-Locs': pandas.Series([t["points"] for t in tp_list1], dtype="object"),
        "Global-Total": pandas.Series([t["total_points"] for t in tp_list1], dtype="Int64"),
        "Country": pandas.Series([t["name"] for t in tp_list2], dtype="object"),
        "Country-Locs": pandas.Series([t["points"] for t in tp_list2], dtype="object"),
        "Contry-Total": pandas.Series([t["total_points"] for t in tp_list2], dtype="Int64"),
        "Region": pandas.Series([t["name"] for t in tp_list3], dtype="object"),
        "Region-Locs": pandas.Series([t["points"] for t in tp_list3], dtype="object"),
        "Region-Total": pandas.Series([t["total_points"] for t in tp_list3], dtype="Int64"),
        "State": pandas.Series([t["name"] for t in tp_list4], dtype="object"),
        "State-Locs": pandas.Series([t["points"] for t in tp_list4], dtype="object"),
        "State-Total": pandas.Series([t["total_points"] for t in tp_list4], dtype="Int64"),
        "Meso": pandas.Series([t["name"] for t in tp_list5], dtype="object"),
        "Meso-Locs": pandas.Series([t["points"] for t in tp_list5], dtype="object"),
        "Meso-Total": pandas.Series([t["total_points"] for t in tp_list5], dtype="Int64")
        })

    # Creates a directory if doesnt exists
    if not os.path.isdir('./results_geonames'):
        os.mkdir('results_geonames')

    writer = ExcelWriter('./results_geonames/' + namefile + '.xlsx')
    final_result.to_excel(writer, 'Sheet1', index=True)
    writer.save()


# Receive a tuple (toponym, lat, lon) and return a Point(lon, lat)
def create_point(item):
    return Point (item[2], item[1])

# Beginning
print("*****************************************************\n")
print("                Focused Gazetteers...\n")
print("*****************************************************\n")

# Initial time
app_time = time.time()

# Create all filter polygons
brasil_polygon         = create_polygons('brasil')
sudeste_polygon        = create_polygons('sudeste')
centro_oeste_polygon   = create_polygons('centro-oeste')
nordeste_polygon       = create_polygons('nordeste')
norte_polygon          = create_polygons('norte')
sul_polygon            = create_polygons('sul') 
ac_polygon   = create_polygons('ac')
al_polygon   = create_polygons('al')
am_polygon   = create_polygons('am')
ap_polygon   = create_polygons('ap')
ba_polygon   = create_polygons('ba')
ce_polygon   = create_polygons('ce')
df_polygon   = create_polygons('df')
es_polygon   = create_polygons('es')
go_polygon   = create_polygons('go')
ma_polygon   = create_polygons('ma')
mg_polygon   = create_polygons('mg')
ms_polygon   = create_polygons('ms')
mt_polygon   = create_polygons('mt')
pa_polygon   = create_polygons('pa')
pb_polygon   = create_polygons('pb')
pe_polygon   = create_polygons('pe')
pi_polygon   = create_polygons('pi')
pr_polygon   = create_polygons('pr')
rj_polygon   = create_polygons('rj')
rn_polygon   = create_polygons('rn')
ro_polygon   = create_polygons('ro')
rs_polygon   = create_polygons('rs')
rr_polygon   = create_polygons('rr')
sc_polygon   = create_polygons('sc')
se_polygon   = create_polygons('se')
sp_polygon   = create_polygons('sp')
to_polygon   = create_polygons('to')
sec_mg_bh_polygon                = create_polygons('mg-bh-e-regiao')
sec_mg_centro_oeste_polygon      = create_polygons('mg-centro-oeste')
sec_mg_grande_minas_polygon      = create_polygons('mg-grande-minas')
sec_mg_sul_de_minas_polygon      = create_polygons('mg-sul-de-minas')
sec_mg_triangulo_polygon         = create_polygons('mg-triangulo-e-alto-paranaiba')
sec_mg_vales_de_minas_polygon    = create_polygons('mg-vales-de-minas')
sec_mg_zona_da_mata_polygon      = create_polygons('mg-zona-da-mata')
sec_pa_belem_polygon             = create_polygons('pa-belem-e-regiao')
sec_pa_santarem_polygon          = create_polygons('pa-santarem-e-regiao')
sec_pe_caruaru_polygon           = create_polygons('pe-caruaru-e-regiao')
sec_pe_petrolina_polygon         = create_polygons('pe-petrolina-e-regiao')
sec_pe_recife_polygon            = create_polygons('pe-recife-e-regiao')
sec_pr_campos_gerais_sul_polygon = create_polygons('pr-campos-gerais-sul')
sec_pr_curitiba_polygon          = create_polygons('pr-curitiba')
sec_pr_norte_noroeste_polygon    = create_polygons('pr-norte-noroeste')
sec_pr_oeste_sudoeste_polygon    = create_polygons('pr-oeste-sudoeste')
sec_rj_norte_fluminense_polygon  = create_polygons('rj-norte-fluminense')
sec_rj_regiao_lagos_polygon      = create_polygons('rj-regiao-dos-lagos')
sec_rj_regiao_serrana_polygon    = create_polygons('rj-regiao-serrana')
sec_rj_rj_polygon                = create_polygons('rj-rj-e-regiao')
sec_rj_sul_do_rio_polygon        = create_polygons('rj-sul-do-rio-e-costa-verde')
sec_sp_bauru_polygon             = create_polygons('sp-bauru-e-marilia')
sec_sp_campinas_polygon          = create_polygons('sp-campinas-e-regiao')
sec_sp_itapetininga_polygon      = create_polygons('sp-itapetininga-e-regiao')
sec_sp_mogi_polygon              = create_polygons('sp-mogi-das-cruzes-e-suzano')
sec_sp_piracicaba_polygon        = create_polygons('sp-piracicaba-e-regiao')
sec_sp_presidente_polygon        = create_polygons('sp-presidente-prudente-e-regiao')
sec_sp_ribeirao_polygon          = create_polygons('sp-ribeirao-preto-e-franca')
sec_sp_santos_polygon            = create_polygons('sp-santos-e-regiao')
sec_sp_sao_carlos_polygon        = create_polygons('sp-sao-carlos-e-araraquara')
sec_sp_sao_jose_polygon          = create_polygons('sp-sao-jose-do-rio-preto-e-aracatuba')
sec_sp_sorocaba_polygon          = create_polygons('sp-sorocaba-e-jundiai')
sec_sp_sp_polygon                = create_polygons('sp-sp-e-regiao')
sec_sp_vale_polygon              = create_polygons('sp-vale-do-paraiba-e-regiao')

# Connect to Geonames db
complete_path = '/home/bruno/workspace/Doutorado/geonames/original/'
conn = sqlite3.connect(complete_path + 'geonames.db')
cursor = conn.cursor()
#cursor.execute("select name, latitude, longitude from geonames where country_code = 'BR';")
cursor.execute("SELECT name, latitude, longitude FROM geonames")

brasil_list = []
norte_list = []
nordeste_list = []
centro_oeste_list = []
sudeste_list = []
sul_list = []
ac_list   = []
al_list   = []
am_list   = []
ap_list   = []
ba_list   = []
ce_list   = []
df_list   = []
es_list   = []
go_list   = []
ma_list   = []
mg_list   = []
ms_list   = []
mt_list   = []
pa_list   = []
pb_list   = []
pe_list   = []
pi_list   = []
pr_list   = []
rj_list   = []
rn_list   = []
ro_list   = []
rs_list   = []
rr_list   = []
sc_list   = []
se_list   = []
sp_list   = []
to_list   = []
sec_mg_bh_list                = []
sec_mg_centro_oeste_list      = []
sec_mg_grande_minas_list      = []
sec_mg_sul_de_minas_list      = []
sec_mg_triangulo_list         = []
sec_mg_vales_de_minas_list    = []
sec_mg_zona_da_mata_list      = []
sec_pa_belem_list             = []
sec_pa_santarem_list          = []
sec_pe_caruaru_list           = []
sec_pe_petrolina_list         = []
sec_pe_recife_list            = []
sec_pr_campos_gerais_sul_list = []
sec_pr_curitiba_list          = []
sec_pr_norte_noroeste_list    = []
sec_pr_oeste_sudoeste_list    = []
sec_rj_norte_fluminense_list  = []
sec_rj_regiao_lagos_list      = []
sec_rj_regiao_serrana_list    = []
sec_rj_rj_list                = []
sec_rj_sul_do_rio_list        = []
sec_sp_bauru_list             = []
sec_sp_campinas_list          = []
sec_sp_itapetininga_list      = []
sec_sp_mogi_list              = []
sec_sp_piracicaba_list        = []
sec_sp_presidente_list        = []
sec_sp_ribeirao_list          = []
sec_sp_santos_list            = []
sec_sp_sao_carlos_list        = []
sec_sp_sao_jose_list          = []
sec_sp_sorocaba_list          = []
sec_sp_sp_list                = []
sec_sp_vale_list              = []

none_brasil_list = []

results = cursor.fetchall()
print(len(results))
for item in tqdm(results):
    tqdm.write(str(item))

    item_point = create_point(item)

    # Country test
    if item_point.within(brasil_polygon):
        brasil_list.append(item)

        # Norte test
        if item_point.within(norte_polygon):
            norte_list.append(item)

            # Acre test
            if item_point.within(ac_polygon):
                ac_list.append(item)

            # Amazonas test
            elif item_point.within(am_polygon):
                am_list.append(item)

            # Amapa test
            elif item_point.within(ap_polygon):
                ap_list.append(item)
            
            # Pará test
            elif item_point.within(pa_polygon):
                pa_list.append(item)

                # Pará-Belém test
                if item_point.within(sec_pa_belem_polygon):
                    sec_pa_belem_list.append(item)

                # Pará-Santarém test
                elif item_point.within(sec_pa_santarem_polygon):
                    sec_pa_santarem_list.append(item)

                else:
                    none_brasil_list.append(item)

            # Tocantins test
            elif item_point.within(to_polygon):
                to_list.append(item)

            # Rondonia test
            elif item_point.within(ro_polygon):
                ro_list.append(item)
        
            # Roraima test
            elif item_point.within(rr_polygon):
                rr_list.append(item)
            
            else:
                none_brasil_list.append(item)
            
        # Nordeste test
        elif item_point.within(nordeste_polygon):
            nordeste_list.append(item)

            # Alagoas Test
            if item_point.within(al_polygon):
                al_list.append(item)

            # Bahia Test
            elif item_point.within(ba_polygon):
                ba_list.append(item)

            # Ceara Test
            elif item_point.within(ce_polygon):
                ce_list.append(item)

            # Maranhão Test
            elif item_point.within(ma_polygon):
                ma_list.append(item)

            # Paraiba Test
            elif item_point.within(pb_polygon):
                pb_list.append(item)

            # Pernambuco Test
            elif item_point.within(pe_polygon):
                pe_list.append(item)

                # Pernambuco-Caruaru Test
                if item_point.within(sec_pe_caruaru_polygon):
                    sec_pe_caruaru_list.append(item)

                # Pernambuco-Petrolina Test
                elif item_point.within(sec_pe_petrolina_polygon):
                    sec_pe_petrolina_list.append(item)

                # Pernambuco-Recife Test
                elif item_point.within(sec_pe_recife_polygon):
                    sec_pe_recife_list.append(item)

                else:
                    none_brasil_list.append(item)

            # Piaui Test
            elif item_point.within(pi_polygon):
                pi_list.append(item)

            # Rio Grande do Norte Test
            elif item_point.within(rn_polygon):
                rn_list.append(item)

            # Sergipe Test
            elif item_point.within(se_polygon):
                se_list.append(item)

            else:
                none_brasil_list.append(item)
            
        # Centro-Oeste test
        elif item_point.within(centro_oeste_polygon):
            centro_oeste_list.append(item)

            # Distrito Federal Test
            if item_point.within(df_polygon):
                df_list.append(item)

            # Goiás Test
            elif item_point.within(go_polygon):
                go_list.append(item)

            # Mato Grosso Test
            elif item_point.within(mt_polygon):
                mt_list.append(item)

            # Mato Grosso do Sul Test
            elif item_point.within(ms_polygon):
                ms_list.append(item)

            else:
                none_brasil_list.append(item)

        # Sudeste test
        elif item_point.within(sudeste_polygon):
            sudeste_list.append(item)

            # Espírito Santo Test
            if item_point.within(es_polygon):
                es_list.append(item)

            # Minas Gerais Test
            elif item_point.within(mg_polygon):
                mg_list.append(item)

                # Minas Gerais-Belo Horizonte Test
                if item_point.within(sec_mg_bh_polygon):
                    sec_mg_bh_list.append(item)

                # Minas Gerais-Centro-Oeste Test
                elif item_point.within(sec_mg_centro_oeste_polygon):
                    sec_mg_centro_oeste_list.append(item)

                # Minas Gerais-Grande Minas Test
                elif item_point.within(sec_mg_grande_minas_polygon):
                    sec_mg_grande_minas_list.append(item)

                # Minas Gerais-Sul de Minas Test
                elif item_point.within(sec_mg_sul_de_minas_polygon):
                    sec_mg_sul_de_minas_list.append(item)

                # Minas Gerais-Triângulo Mineiro Test
                elif item_point.within(sec_mg_triangulo_polygon):
                    sec_mg_triangulo_list.append(item)

                # Minas Gerais-Vales de Minas Test
                elif item_point.within(sec_mg_vales_de_minas_polygon):
                    sec_mg_vales_de_minas_list.append(item)

                # Minas Gerais-Zona da Mata Test
                elif item_point.within(sec_mg_zona_da_mata_polygon):
                    sec_mg_zona_da_mata_list.append(item)

                else:
                    none_brasil_list.append(item)

            # Rio de Janeiro Test
            elif item_point.within(rj_polygon):
                rj_list.append(item)

                # Rio de Janeiro-Norte Fluminense Test
                if item_point.within(sec_rj_norte_fluminense_polygon):
                    sec_rj_norte_fluminense_list.append(item)

                # Rio de Janeiro-Região dos Lagos Test
                elif item_point.within(sec_rj_regiao_lagos_polygon):
                    sec_rj_regiao_lagos_list.append(item)

                # Rio de Janeiro-Região Serrana Test
                elif item_point.within(sec_rj_regiao_serrana_polygon):
                    sec_rj_regiao_serrana_list.append(item)

                # Rio de Janeiro-RJ Test
                elif item_point.within(sec_rj_rj_polygon):
                    sec_rj_rj_list.append(item)

                # Rio de Janeiro-Sul do Rio e Costa Sul Test
                elif item_point.within(sec_rj_sul_do_rio_polygon):
                    sec_rj_sul_do_rio_list.append(item)
                    
                else:
                    none_brasil_list.append(item)

            # São Paulo Test
            elif item_point.within(sp_polygon):
                sp_list.append(item)

                # São Paulo-Bauru e Marília Test
                if item_point.within(sec_sp_bauru_polygon):
                    sec_sp_bauru_list.append(item)

                # São Paulo-Campinas Test
                elif item_point.within(sec_sp_campinas_polygon):
                    sec_sp_campinas_list.append(item)

                # São Paulo-Itapetinga Test
                elif item_point.within(sec_sp_itapetininga_polygon):
                    sec_sp_itapetininga_list.append(item)

                # São Paulo-Mogi das Cruzes Test
                elif item_point.within(sec_sp_mogi_polygon):
                    sec_sp_mogi_list.append(item)

                # São Paulo-Piracicaba Test
                elif item_point.within(sec_sp_piracicaba_polygon):
                    sec_sp_piracicaba_list.append(item)

                # São Paulo-Presidente Prudente Test
                elif item_point.within(sec_sp_presidente_polygon):
                    sec_sp_presidente_list.append(item)

                # São Paulo-Ribeirão Preto Test
                elif item_point.within(sec_sp_ribeirao_polygon):
                    sec_sp_ribeirao_list.append(item)

                # São Paulo-Santos Test
                elif item_point.within(sec_sp_santos_polygon):
                    sec_sp_santos_list.append(item)

                # São Paulo-São Carlos Test
                elif item_point.within(sec_sp_sao_carlos_polygon):
                    sec_sp_sao_carlos_list.append(item)

                # São Paulo-São José dos Campos Test
                elif item_point.within(sec_sp_sao_jose_polygon):
                    sec_sp_sao_jose_list.append(item)

                # São Paulo-Sorocaba Test
                elif item_point.within(sec_sp_sorocaba_polygon):
                    sec_sp_sorocaba_list.append(item)

                # São Paulo-SP Test
                elif item_point.within(sec_sp_sp_polygon):
                    sec_sp_sp_list.append(item)

                # São Paulo-Vale da Paraíba Test
                elif item_point.within(sec_sp_vale_polygon):
                    sec_sp_vale_list.append(item)

                else:
                    none_brasil_list.append(item)

        # Sul test
        elif item_point.within(sul_polygon):
            sul_list.append(item)

            # Paraná Test
            if item_point.within(pr_polygon):
                pr_list.append(item)

                # Paraná-Campos Gerais Test
                if item_point.within(sec_pr_campos_gerais_sul_polygon):
                    sec_pr_campos_gerais_sul_list.append(item)

                # Paraná-Curitiba Test
                elif item_point.within(sec_pr_curitiba_polygon):
                    sec_pr_curitiba_list.append(item)

                # Paraná-Norte e Noroeste Test
                elif item_point.within(sec_pr_norte_noroeste_polygon):
                    sec_pr_norte_noroeste_list.append(item)

                # Paraná-Oeste e Sudoeste Test
                elif item_point.within(sec_pr_oeste_sudoeste_polygon):
                    sec_pr_oeste_sudoeste_list.append(item)
                
                # Não está no Paraná
                else:
                    none_brasil_list.append(item)
        
            # Santa Catarina Test
            elif item_point.within(sc_polygon):
                sc_list.append(item)

            # Rio Grande do Sul Test
            elif item_point.within(rs_polygon):
                rs_list.append(item)

            else:
                none_brasil_list.append(item)
        
        # Nenhuma das Regiões
        else:
            none_brasil_list.append(item)

    # Não é Brasil
    else:
        none_brasil_list.append(item)
    

tqdm.write("-- total time: %.05f seconds --\n" % (time.time() - app_time))

print("Country list: %i" % len(brasil_list))

print("\nNorte list: %i" % len(norte_list))
print("\tAcre list: %i" % len(ac_list))
print("\tAmazonas list: %i" % len(am_list))
print("\tPará list: %i" % len(pa_list))
print("\t\tPará-Belém list: %i" % len(sec_pa_belem_list))
print("\t\tPará-Santarém list: %i" % len(sec_pa_santarem_list))
print("\tRondônia list: %i" % len(ro_list))
print("\tRoraima list: %i" % len(rr_list))
print("\tTocantins list: %i" % len(to_list))

print("\nNordeste list: %i" % len(nordeste_list))
print("\tAlagoas list: %i" % len(al_list))
print("\tBahia list: %i" % len(ba_list))
print("\tCeará list: %i" % len(ce_list))
print("\tMaranhão list: %i" % len(ma_list))
print("\tParaíba list: %i" % len(pb_list))
print("\tPiauí list: %i" % len(pi_list))
print("\tPernambuco list: %i" % len(ma_list))
print("\t\tPerbambuco-Caruaru: %i" % len(sec_pe_caruaru_list))
print("\t\tPerbambuco-Petrolina: %i" % len(sec_pe_petrolina_list))
print("\t\tPerbambuco-Recife: %i" % len(sec_pe_recife_list))
print("\tRio Grande do Norte: %i" % len(rn_list))
print("\tSergipe list: %i" % len(se_list))

print("\nCentro-Oste list: %i" % len(centro_oeste_list))
print("\tDistrito Federal: %i" % len(df_list))
print("\tGoiás: %i" % len(go_list))
print("\tMato Grosso: %i" % len(mt_list))
print("\tMato Grosso do Sul: %i" % len(ms_list))

print("\nSudeste list: %i" % len(sudeste_list))
print("\tEspírito Santo: %i" % len(es_list))
print("\tMinas Gerais: %i" % len(mg_list))
print("\t\tMinas Gerais-BH: %i" % len(sec_mg_bh_list))
print("\t\tMinas Gerais-Centro-Oeste: %i" % len(sec_mg_centro_oeste_list))
print("\t\tMinas Gerais-Grande Minas: %i" % len(sec_mg_grande_minas_list))
print("\t\tMinas Gerais-Sul de Minas: %i" % len(sec_mg_sul_de_minas_list))
print("\t\tMinas Gerais-Triângulo Mineiro: %i" % len(sec_mg_triangulo_list))
print("\t\tMinas Gerais-Vales de Minas: %i" % len(sec_mg_vales_de_minas_list))
print("\t\tMinas Gerais-Zona da Mata: %i" % len(sec_mg_zona_da_mata_list))
print("\tRio de Janeiro: %i" % len(rj_list))
print("\t\tRio de Janeiro-Norte Fluminense: %i" % len(sec_rj_norte_fluminense_list))
print("\t\tRio de Janeiro-Região dos Lagos: %i" % len(sec_rj_regiao_lagos_list))
print("\t\tRio de Janeiro-Região Serrana: %i" % len(sec_rj_regiao_serrana_list))
print("\t\tRio de Janeiro-RJ: %i" % len(sec_rj_rj_list))
print("\t\tRio de Janeiro-Sul do Rio: %i" % len(sec_rj_sul_do_rio_list))
print("\tSão Paulo: %i" % len(sp_list))
print("\t\tSão Paulo-Bauru: %i" % len(sec_sp_bauru_list))
print("\t\tSão Paulo-Campinas: %i" % len(sec_sp_campinas_list))
print("\t\tSão Paulo-Itapetinga: %i" % len(sec_sp_itapetininga_list))
print("\t\tSão Paulo-Mogi das Cruzes: %i" % len(sec_sp_mogi_list))
print("\t\tSão Paulo-Piracicaba: %i" % len(sec_sp_piracicaba_list))
print("\t\tSão Paulo-Presidente Prudente: %i" % len(sec_sp_presidente_list))
print("\t\tSão Paulo-Ribeirão Preto: %i" % len(sec_sp_ribeirao_list))
print("\t\tSão Paulo-Santos: %i" % len(sec_sp_santos_list))
print("\t\tSão Paulo-São Carlos: %i" % len(sec_sp_sao_carlos_list))
print("\t\tSão Paulo-São José do Rio Preto: %i" % len(sec_sp_sao_jose_list))
print("\t\tSão Paulo-Sorocaba: %i" % len(sec_sp_sorocaba_list))
print("\t\tSão Paulo-SP: %i" % len(sec_sp_sp_list))
print("\t\tSão Paulo-Vale do Paraíba: %i" % len(sec_sp_vale_list))


print("\nSul list: %i" % len(sul_list))
print("\tParaná: %i" % len(pr_list))
print("\t\tParaná-Campos Gerais: %i" % len(sec_pr_campos_gerais_sul_list))
print("\t\tParaná-Curitiba: %i" % len(sec_pr_curitiba_list))
print("\t\tParaná-Norte e Noroeste: %i" % len(sec_pr_norte_noroeste_list))
print("\t\tParaná-Oeste e Sudoeste: %i" % len(sec_pr_oeste_sudoeste_list))
print("\tSanta Catarina: %i" % len(sc_list))
print("\tRio Grande do Sul: %i" % len(rs_list))