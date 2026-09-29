CB,CA,CI,EN,GA,GI,HE,IN,NE,NR,NL,OF,PE,PS,RE,SP,TR="ciencias_basicas","cardiologia","cirugia","endocrinologia","gastroenterologia","ginecologia","hematologia","infectologia","nefrologia","neumologia","neurologia","oftalmo_orl","pediatria","psiquiatria","reumatologia","salud_publica","traumatologia"
# (n del PDF, archivo, tema, letra correcta revisada)
SEL=[]
def add(*t): SEL.extend(t)
COM={}
OPT={}
ENU={}
EXC={}

# --- v00 ---
add((1840,RE,"Acné grave: nódulos y quistes","B"),
(1847,GA,"Peritonitis bacteriana espontánea con alergia a cefalosporinas: fluoroquinolona","D"),
(1851,CB,"Hidroperoxidasas: protección frente a los radicales libres","C"),
(1859,PE,"Giardiasis: metronidazol","B"),
(1898,GI,"Saco gestacional pequeño sin embrión: control ecográfico","D"),
(1924,TR,"Luxación posterior de cadera: lesión del nervio ciático","A"),
(1933,CB,"Cicatrización: el fibroblasto","D"))
OPT[1851]={"C":"Hidroperoxidasas"}
COM[1851]="Las hidroperoxidasas (peroxidasas y catalasa) protegen al organismo frente a los peróxidos y los radicales libres: descomponen el peróxido de hidrógeno y los peróxidos lipídicos generados en el metabolismo, evitando el estrés oxidativo. Las oxidasas y deshidrogenasas transfieren electrones o hidrógeno en reacciones de oxidación-reducción, y las oxigenasas incorporan oxígeno a los sustratos; ninguna tiene como función principal la protección antioxidante."
COM[1847]="Cirrótico con fiebre, dolor abdominal y líquido ascítico con ≥250 neutrófilos/mm³ (aquí 500): peritonitis bacteriana espontánea. El tratamiento empírico de elección es una cefalosporina de tercera generación, pero el paciente es alérgico a la ceftriaxona. La alternativa es una fluoroquinolona (ciprofloxacino o levofloxacino), siempre que no la haya recibido como profilaxis. Se asocia albúmina EV porque la creatinina está elevada (>1 mg/dL), para prevenir el síndrome hepatorrenal."
EXC.update({1842:"mismo concepto ya publicado (GIN-059)",1852:"mismo concepto ya publicado (INF-053)",1853:"mismo concepto ya publicado (SP-058)",
1854:"mismo concepto ya publicado (PED-192)",1858:"mismo concepto ya publicado (OFT-008)",1862:"mismo concepto ya publicado (INF, bloque 7) y opción vacía",
1873:"clave ambigua",1879:"mismo concepto ya publicado (GIN-096)",1880:"mismo concepto ya publicado (REU-028)",1895:"mismo concepto ya publicado (NEU-026)",
1906:"mismo concepto ya publicado (NEU-024)",1907:"mismo concepto ya publicado (NEU-054)",1913:"mismo concepto ya publicado (GIN-085)",1919:"clave discutible",
1920:"mismo concepto ya publicado (PED-198)",1923:"mismo concepto ya publicado (OFT-020)",1925:"mismo concepto ya publicado (PED-095)",1926:"clave dudosa",
1927:"clave discutible (AHA: RCP si queda inconsciente)",1929:"mismo concepto ya publicado (REU-030)",1935:"mismo concepto ya publicado (GIN-182)",
1936:"mismo concepto ya publicado (INF-056)",1938:"mismo concepto ya publicado (REU-060)",1939:"mismo concepto ya publicado (GIN-086)",
1941:"mismo concepto ya publicado (HEM-039)",1943:"mismo concepto ya publicado (HEM-022)",1945:"clave discutible",1948:"clave dudosa (escenarios MINSA)",
1949:"mismo concepto ya publicado (INF-051)",1950:"mismo concepto ya publicado (PED-143)",1951:"mismo concepto ya publicado (OFT-002)",1957:"clave dudosa",
1962:"mismo concepto ya publicado (GIN-077)"})

# --- v01 ---
add((1986,CB,"Toxicidad por anestésicos locales: oxígeno primero","D"),
(1994,NL,"Escala de Glasgow: 8 puntos","C"),
(1999,PE,"Encefalopatía hipóxico-isquémica grave: hipotermia terapéutica","C"),
(2003,PE,"Anemia ferropénica del lactante: hierro oral","C"),
(2031,PE,"Síndrome nefrótico infantil: enfermedad de cambios mínimos","D"),
(2039,SP,"Aborto terapéutico por riesgo materno: beneficencia","D"),
(2045,SP,"Parto con pertinencia cultural: destino de la placenta","D"),
(2046,CB,"Imipenem en insuficiencia renal: convulsiones","A"),
(2048,SP,"Ensayo clínico fase IV: vigilancia poscomercialización","C"))
ENU[1994]="Varón de 20 años politraumatizado por accidente de moto hace una hora. Hemodinámicamente estable. Examen neurológico: abre los ojos y retira las manos solo ante el estímulo doloroso y emite sonidos incomprensibles. ¿Qué puntaje en la escala de Glasgow le corresponde?"
COM[1986]="Hormigueo peribucal y de la lengua, desorientación, hipotensión y SatO₂ de 90 % tras infiltrar lidocaína: toxicidad sistémica por anestésicos locales. Lo primero es detener la administración, pedir ayuda y asegurar la vía aérea con oxígeno al 100 %, porque la hipoxia y la acidosis agravan la toxicidad neurológica y cardiaca. Si aparecen convulsiones se usan benzodiacepinas, y ante toxicidad grave o colapso cardiovascular se administra emulsión lipídica al 20 %. La hidrocortisona no tiene papel: no es una reacción alérgica."
COM[1994]="La escala de Glasgow suma apertura ocular (1-4), respuesta verbal (1-5) y respuesta motora (1-6). Este paciente abre los ojos solo al dolor (O2), emite sonidos incomprensibles (V2) y retira la mano ante el dolor (M4): 2 + 2 + 4 = 8 puntos. Un Glasgow de 8 o menos define un traumatismo craneoencefálico grave e indica asegurar la vía aérea con intubación."
COM[2003]="Lactante de 11 meses con Hb 9 g/dL, anemia microcítica e hipocrómica y ferritina baja: anemia ferropénica. El tratamiento es hierro por vía oral, a 3 mg/kg/día de hierro elemental (sulfato ferroso o complejo polimaltosado férrico), durante 6 meses continuos según la norma MINSA, con control de hemoglobina al mes, a los 3 y a los 6 meses, junto con consejería para dar alimentos de origen animal ricos en hierro. La cianocobalamina y el ácido fólico tratan las anemias megaloblásticas y la eritropoyetina se reserva para la anemia de la enfermedad renal crónica."
COM[2046]="Paciente con insuficiencia renal tratado por pielonefritis que presenta convulsiones: el fármaco más relacionado es el imipenem. Este carbapenémico disminuye el umbral convulsivo al antagonizar los receptores GABA-A, y el riesgo aumenta cuando se acumula por falla renal sin ajustar la dosis o hay enfermedad del sistema nervioso central. La ceftriaxona, la amikacina y la ampicilina a dosis habituales rara vez producen convulsiones; la amikacina se asocia más a nefrotoxicidad y ototoxicidad."
COM[2048]="La fase IV del ensayo clínico (farmacovigilancia poscomercialización) se realiza después de que el fármaco ha sido aprobado y comercializado. Busca efectos adversos raros o graves y datos de seguridad a largo plazo en poblaciones grandes y variadas, que no se detectan en las fases previas por su tamaño limitado. La fase I evalúa seguridad y farmacocinética en pocos voluntarios, la fase II eficacia y dosis, y la fase III compara el nuevo tratamiento con el estándar antes de la aprobación."
EXC.update({1965:"mismo concepto ya publicado (NEF-071)",1966:"clave dudosa",1968:"mismo concepto ya publicado (CB-023)",1969:"mismo concepto ya publicado (PED-212)",
1970:"clave ambigua",1972:"clave ambigua",1973:"mismo concepto ya publicado (PED-065)",1974:"mismo concepto ya publicado (GAS-037)",1975:"clave ambigua",
1978:"mismo concepto ya publicado (GIN-205)",1979:"clave ambigua",1980:"mismo concepto ya publicado (TRA-031)",1984:"mismo concepto ya publicado (CB-024)",
1985:"clave dudosa",1988:"mismo concepto ya publicado (PED-197)",1989:"mismo concepto ya publicado (PED-096)",1992:"mismo concepto ya publicado (PED-035)",
1993:"mismo concepto ya publicado (GIN-222)",1995:"mismo concepto ya publicado (CB-049)",1996:"mismo concepto ya publicado (CIR-089)",
1997:"mismo concepto ya publicado (GIN-201)",1998:"mismo concepto ya publicado (NEU-015)",2001:"mismo concepto ya publicado (GIN-111)",
2009:"mismo concepto ya publicado (CIR-029)",2010:"mismo concepto ya publicado (TRA-040)",2011:"mismo concepto ya publicado (GIN-059)",
2018:"mismo concepto ya publicado (REU-060)",2019:"mismo concepto ya publicado (INF-056)",2025:"mismo concepto ya publicado (GIN-125)",
2026:"mismo concepto ya publicado (SP-031)",2028:"mismo concepto ya publicado (GIN-031)",2030:"mismo concepto ya publicado (CIR-035)",
2035:"mismo concepto ya publicado (GIN-040)",2038:"mismo concepto ya publicado (REU-037)",2041:"mismo concepto ya publicado (CIR-020)",
2044:"mismo concepto ya publicado (CAR-064)"})

# --- v02 ---
add((2063,SP,"Modelo de Cuidado Integral de Salud: enfoque intercultural","A"),
(2064,GI,"Prolapso de cúpula vaginal tras histerectomía","B"),
(2074,SP,"Curación sin guantes: falta al principio de no maleficencia","A"),
(2076,CB,"Urticaria aguda por amoxicilina: hipersensibilidad tipo I","D"),
(2083,PS,"Bulimia nerviosa: hipopotasemia","D"),
(2084,CI,"Acceso vascular percutáneo: arteria femoral común","C"),
(2087,NE,"Tumor testicular: marcadores tumorales (β-hCG)","A"),
(2091,SP,"Consentimiento informado por escrito: principio de autonomía","A"),
(2092,IN,"Accidente punzocortante del personal de salud: exposición ocupacional","C"),
(2093,IN,"Sífilis secundaria: penicilina benzatínica","B"),
(2094,GI,"Preeclampsia con signos de severidad en el primer nivel: sulfato de magnesio y referir","B"),
(2102,NE,"Cólico renal: analgesia","B"),
(2105,TR,"Fractura abierta: antibióticos precoces","C"),
(2106,NE,"Pielonefritis que no mejora con antibiótico adecuado: absceso renal","C"),
(2111,NR,"Neumonía atípica: macrólido","D"),
(2114,SP,"UPSS obligatoria en el establecimiento I-4: patología clínica","A"),
(2116,CB,"Loxoscelismo cutáneo-visceral: hidratación enérgica","B"),
(2118,TR,"Fractura supracondílea no desplazada del adulto: férula con codo a 90°","C"))
OPT[2064]={"D":"Rectocele"}
OPT[2076]={"D":"I"}
COM[2064]="Mujer con histerectomía vaginal previa y sensación de bulto vaginal. En el sistema POP-Q, el punto C marca el cuello uterino o, si no hay útero, la cúpula vaginal. Un punto C en +6 significa que la cúpula desciende 6 cm por fuera del himen: es un prolapso de cúpula vaginal (compartimento apical). El cistocele y el uretrocele afectan la pared anterior (puntos Aa y Ba) y el rectocele la pared posterior (puntos Ap y Bp)."
COM[2076]="Ronchas pruriginosas (habones) que aparecen a los 30 minutos de recibir amoxicilina corresponden a una urticaria aguda por reacción de hipersensibilidad tipo I de Gell y Coombs. Es inmediata y está mediada por IgE: el alérgeno se une a la IgE fijada en mastocitos y basófilos, que liberan histamina y otros mediadores. La tipo II es citotóxica por anticuerpos, la tipo III por inmunocomplejos y la tipo IV es tardía, mediada por linfocitos T."
COM[2093]="Úlcera genital indolora que curó sola hace 2 meses (chancro) y ahora fiebre con pápulas marrones en palmas: sífilis secundaria, confirmada por RPR 1/320 y TPHA reactivo. El tratamiento de elección de la sífilis temprana (primaria, secundaria o latente precoz) es penicilina G benzatínica 2,4 millones UI IM en dosis única. La ceftriaxona y la azitromicina son alternativas solo ante alergia a penicilina, y el ciprofloxacino no trata la sífilis."
COM[2102]="Dolor lumbar tipo cólico irradiado a genitales, orina oscura y puñopercusión positiva en una paciente con episodios previos: cólico renal por litiasis. El tratamiento inicial es la analgesia, de preferencia con AINE (diclofenaco o ketorolaco) y, si no basta, opioides, junto con una hidratación adecuada (sin forzar líquidos). La litotricia extracorpórea se reserva para cálculos que no se expulsan, y no están indicados los diuréticos. Los antibióticos solo se usan si hay infección asociada."
COM[2114]="Según la norma técnica de categorización del MINSA, el establecimiento I-4 debe contar obligatoriamente con las UPSS de consulta externa, patología clínica (laboratorio clínico), farmacia e internamiento. El centro quirúrgico es opcional en el I-4. El banco de sangre y las unidades de cuidados intensivos corresponden a establecimientos de mayor complejidad, del segundo y tercer nivel."
COM[2118]="Fractura supracondílea del húmero con desplazamiento mínimo en una paciente adulta mayor: se puede manejar de forma conservadora con una férula braquiopalmar posterior con el codo en flexión de 90° y el antebrazo en posición neutra, vigilando el estado neurovascular. La férula colgante y la de coaptación se usan en las fracturas de la diáfisis del húmero, y la fijación con placas se reserva para fracturas desplazadas o inestables."
EXC.update({2049:"mismo concepto ya publicado (CIR-095)",2051:"mismo concepto ya publicado (GAS-040)",2052:"mismo concepto ya publicado (HEM-008)",
2053:"mismo concepto ya publicado (SP-076)",2054:"mismo concepto ya publicado (HEM-026)",2058:"mismo concepto ya publicado (NEF-041)",2060:"clave dudosa",
2061:"mismo concepto ya publicado (GIN-094)",2069:"mismo concepto ya publicado (PED-147)",2072:"clave ambigua (NEF-081 indica hemodiálisis)",
2073:"clave ambigua",2075:"mismo concepto ya publicado (TRA-014)",2079:"mismo concepto ya publicado (PED-152)",2081:"mismo concepto ya publicado (GIN-096)",
2085:"clave ambigua",2086:"mismo concepto ya publicado (PED-134)",2088:"mismo concepto ya publicado (REU-040)",2090:"mismo concepto ya publicado (GIN-123)",
2095:"mismo concepto ya publicado (GAS-026)",2097:"mismo concepto ya publicado (GIN-035)",2099:"mismo concepto ya publicado (REU-045)",
2100:"clave dudosa (escala de crup)",2103:"mismo concepto ya publicado (CAR-032)",2107:"mismo concepto ya publicado (SP-068)",2108:"clave ambigua (brote/epidemia)",
2112:"mismo concepto ya publicado (PED-052)",2113:"mismo concepto ya publicado (TRA-041)"})

# --- v03 ---
add((2119,CB,"Osteoclasto: célula multinucleada de la resorción ósea","C"),
(2124,SP,"Dengue en asentamientos sin agua potable: abordar determinantes sociales","D"),
(2127,RE,"Cáncer de piel: radiación ultravioleta","B"),
(2132,EN,"DM2 de debut con hiperglucemia sintomática grave: insulina","C"),
(2134,IN,"Vacuna contra la fiebre amarilla: al menos 10 días antes del viaje","D"),
(2135,PE,"Colitis hemorrágica con síndrome urémico hemolítico: E. coli productora de toxina Shiga","A"),
(2148,GI,"Test no estresante reactivo","A"),
(2152,GI,"POP-Q: el punto Aa corresponde a la unión uretrovesical","C"),
(2154,CI,"Flegmasía alba dolens","B"),
(2159,PE,"Otitis media aguda en menores de 2 años: 10 días de antibiótico","D"),
(2165,GI,"Síndrome HELLP: riesgo de desprendimiento prematuro de placenta","A"),
(2167,IN,"Proctitis tras coito anal receptivo: gonococo","A"),
(2176,SP,"Educación escolar contra el dengue: eliminar criaderos","B"),
(2178,NR,"Hemoptisis en fumador: tomografía de tórax","C"))
COM[2119]="Las células gigantes multinucleadas que reabsorben el hueso son los osteoclastos. Derivan de la línea monocito-macrófago, se ubican en las lagunas de Howship y degradan la matriz ósea mediante enzimas y ácido. Los osteoblastos forman hueso y los osteocitos son osteoblastos maduros atrapados en la matriz. Los megacariocitos también son células grandes de la médula ósea, pero tienen un núcleo único multilobulado (poliploide) y producen plaquetas, no reabsorben hueso."
COM[2127]="El principal factor de riesgo del cáncer de piel (carcinoma basocelular, espinocelular y melanoma) es la exposición a la radiación ultravioleta solar, sobre todo acumulada e intermitente intensa, con quemaduras. Los militares jóvenes que realizan actividades prolongadas al aire libre sin fotoprotección están especialmente expuestos. El benceno se asocia a leucemias, la radiación ionizante a leucemias y cáncer de tiroides, y la contaminación del agua con arsénico a lesiones cutáneas, pero no explican este aumento."
COM[2148]="El test no estresante (NST) evalúa la reactividad de la frecuencia cardiaca fetal. Es reactivo cuando en 20 minutos hay al menos 2 aceleraciones (≥15 latidos por 15 segundos a término) asociadas a movimientos fetales, con variabilidad normal y sin desaceleraciones: indica bienestar fetal. Los términos positivo y negativo se usan para el test estresante (prueba de tolerancia a las contracciones), no para el NST. Es no reactivo si no cumple esos criterios tras 40 minutos."
COM[2152]="En el sistema POP-Q, el punto Aa se ubica en la línea media de la pared vaginal anterior, 3 cm proximal al meato uretral externo, y corresponde aproximadamente a la unión uretrovesical. Su rango va de -3 a +3. El punto Ba es el punto más declive del resto de la pared anterior, el punto C es el cuello uterino (o la cúpula tras la histerectomía) y el punto D el fondo de saco posterior (fórnix posterior)."
COM[2154]="Paciente postrado por fractura de cadera, con trombosis venosa profunda confirmada por dúplex, edema masivo doloroso de toda la pierna y coloración blanquecina: flegmasía alba dolens. Se debe a una trombosis iliofemoral extensa con espasmo arterial reflejo, sin isquemia establecida. Si la obstrucción venosa progresa y compromete la circulación, la pierna se vuelve cianótica y aparece la flegmasía cerúlea dolens, con riesgo de gangrena venosa. La tromboflebitis superficial afecta venas subcutáneas y no produce edema masivo."
COM[2159]="Lactante de 18 meses con otitis media aguda tratado con amoxicilina a 90 mg/kg/día. En menores de 2 años (y en casos graves o con otorrea) se recomienda un tratamiento de 10 días, porque los esquemas cortos tienen más fracasos en este grupo. En niños de 2 a 5 años con cuadro leve o moderado se pueden usar 7 días, y en mayores de 6 años, 5 a 7 días."
COM[2165]="Primigesta de 38 semanas con PA de 160/100 mmHg, cefalea, escotomas, plaquetas de 80 000, transaminasas elevadas y DHL de 700 UI/L: preeclampsia con signos de severidad y síndrome HELLP. Entre las opciones, la complicación más probable es el desprendimiento prematuro de placenta normoinserta, cuyo riesgo aumenta por la hipertensión grave y el daño endotelial. Otras complicaciones del HELLP son la CID, la eclampsia, el hematoma hepático, la insuficiencia renal y el edema pulmonar. La placenta previa y la rotura de membranas no guardan relación con la preeclampsia."
COM[2167]="Proctitis aguda (dolor anal, tenesmo o urgencia defecatoria y secreción mucopurulenta) pocos días después de un coito anal receptivo: es una infección de transmisión sexual, y el agente más frecuente es Neisseria gonorrhoeae, seguido de Chlamydia trachomatis. Se trata empíricamente con ceftriaxona más doxiciclina. Treponema pallidum produce un chancro anal, Cryptosporidium diarrea acuosa, y Yersinia una enterocolitis por alimentos, no una proctitis de transmisión sexual."
COM[2176]="En una zona de alta incidencia de dengue, la acción educativa prioritaria con los escolares es promover la eliminación de criaderos del Aedes aegypti en el hogar y la escuela (tapar, lavar y escobillar recipientes con agua, desechar inservibles). Así los alumnos se vuelven agentes de cambio en sus familias y se reduce la transmisión. Conocer los signos de alarma y evitar la automedicación es útil para el manejo del enfermo, pero no disminuye la aparición de casos."
COM[2178]="Varón fumador pesado de 55 años con tos, disnea, hemoptisis, hipoventilación localizada y sibilancias unilaterales (sugieren obstrucción bronquial): se debe descartar un cáncer de pulmón. Entre las opciones, el examen inicial indicado es la tomografía de tórax con contraste, que caracteriza la lesión, los ganglios y guía la broncoscopia para obtener biopsia. El PET se usa después para la estadificación, y la gammagrafía y la ecografía pulmonar no sirven para evaluar una masa central."
EXC.update({2120:"mismo concepto que otra aceptada (2093)",2122:"mismo concepto ya publicado (GAS-034)",2123:"mismo concepto ya publicado (CAR-028)",
2126:"mismo concepto ya publicado (NRL-026)",2130:"mismo concepto ya publicado (OFT-008)",2131:"mismo concepto ya publicado (GIN-210)",
2133:"mismo concepto ya publicado (REU-017)",2139:"mismo concepto ya publicado (NRL-004)",2142:"mismo concepto ya publicado (GIN-209)",
2143:"mismo concepto ya publicado (HEM-021)",2144:"mismo concepto ya publicado (TRA-046)",2147:"clave dudosa",2149:"mismo concepto ya publicado (GAS-072)",
2150:"mismo concepto ya publicado (GIN-069)",2151:"mismo concepto ya publicado (GAS-045)",2153:"mismo concepto ya publicado (TRA-042)",
2155:"mismo concepto ya publicado (HEM-022)",2156:"mismo concepto ya publicado (PED-033)",2157:"mismo concepto ya publicado (PED-006)",
2160:"mismo concepto ya publicado (OFT-015)",2161:"mismo concepto ya publicado (SP-031)",2163:"mismo concepto ya publicado (CIR-050)",
2164:"mismo concepto ya publicado (REU-017)",2168:"mismo concepto ya publicado (REU-013)",2169:"clave ambigua",2171:"mismo concepto ya publicado (INF-055)",
2173:"clave ambigua",2174:"mismo concepto ya publicado (SP-018)",2175:"mismo concepto ya publicado (GIN-214)",2179:"mismo concepto ya publicado (PED-069)",
2180:"clave ambigua"})

# --- v04 ---
add((2185,CB,"Hidroxicobalamina: orina de color rojo","A"),
(2188,TR,"Fractura de pelvis inestable con shock: estabilizar la pelvis","A"),
(2193,GI,"Diabetes gestacional sin control con dieta: insulina","D"),
(2196,IN,"Tuberculosis con baciloscopía positiva al cuarto mes: fracaso","C"),
(2208,CI,"Absceso perianal fluctuante: drenaje","D"),
(2211,EN,"Diabetes confirmada por dos glucemias en ayunas ≥126 mg/dL: metformina","B"),
(2217,PE,"Hijo de madre diabética: hipoglucemia por hiperinsulinismo","B"),
(2218,NR,"Exacerbación de EPOC con hipercapnia: broncodilatadores, corticoides y oxígeno controlado","B"),
(2221,NE,"Litiasis ureteral: enclavamiento en la unión ureterovesical","B"),
(2224,PE,"Cardiopatías con cortocircuito de izquierda a derecha: Qp/Qs mayor que 1","B"),
(2231,PE,"Alergia a las proteínas de la leche de vaca","A"),
(2233,OF,"Conjuntivitis química por cloro de piscina","B"),
(2234,PE,"Acalasia: signo del pico de pájaro","D"),
(2237,SP,"Liderazgo autoritario","A"))
COM[2185]="Bombero expuesto al humo de un incendio de plásticos: puede tener intoxicación por monóxido de carbono y también por cianuro, por lo que se trata con oxígeno a alto flujo e hidroxicobalamina, el antídoto del cianuro. La hidroxicobalamina es un compuesto de color rojo intenso que se elimina por la orina y la tiñe de rojo (cromaturia), además de dar coloración rojiza a la piel; es un efecto esperado y benigno. No indica hematuria ni mioglobinuria, aunque puede interferir con algunas pruebas colorimétricas."
COM[2196]="Según la norma técnica de tuberculosis del MINSA, se considera fracaso al tratamiento de la TB sensible cuando la baciloscopía o el cultivo siguen positivos a partir del cuarto mes de tratamiento (o se positivizan de nuevo tras haberse negativizado). Esta paciente, en su cuarto mes con baciloscopía positiva, es un fracaso bacteriológico: se debe solicitar prueba de sensibilidad (molecular y convencional) para descartar resistencia. La conversión es la negativización del esputo, y la pérdida en el seguimiento es la interrupción del tratamiento por 30 días o más."
COM[2211]="El diagnóstico de diabetes se confirma con dos glucemias en ayunas ≥126 mg/dL en días distintos. Este paciente tiene 153 y 146 mg/dL (la de 115 mg/dL corresponde a glucosa alterada en ayunas), por lo que ya es diabético. Por ser obeso, asintomático y sin descompensación, se inicia metformina junto con cambios en el estilo de vida (dieta y actividad física). No corresponde esperar un mes, la insulina se reserva para hiperglucemia grave o sintomática y el péptido C no es necesario para el diagnóstico."
COM[2217]="En el hijo de madre diabética, la hiperglucemia materna atraviesa la placenta y estimula de forma sostenida las células beta del páncreas fetal, que se hiperplasian y producen hiperinsulinismo. Al nacer se corta bruscamente el aporte de glucosa materna, pero la insulina sigue alta, lo que causa hipoglucemia en las primeras horas de vida. Por eso se vigila la glucemia desde el nacimiento y se inicia alimentación precoz. Hay hiperplasia, no hipotrofia, de las células beta."
COM[2218]="EPOC con exacerbación aguda y acidosis respiratoria (pH 7,29, pCO₂ 65 mmHg) sin neumonía: se trata con broncodilatadores de acción corta (salbutamol e ipratropio), corticoides sistémicos (prednisona 40 mg por 5 días) y oxígeno controlado para una SatO₂ de 88-92 %, porque el oxígeno a alto flujo puede empeorar la hipercapnia. Con pH <7,35 y pCO₂ >45 mmHg está indicada además la ventilación no invasiva. Los antibióticos se indican si aumenta la purulencia del esputo, y los mucolíticos no forman parte del manejo agudo."
COM[2221]="El uréter tiene tres estrechamientos fisiológicos donde se detienen los cálculos: la unión pieloureteral, el cruce con los vasos ilíacos y la unión ureterovesical. La unión ureterovesical es el segmento más estrecho y el sitio donde con mayor frecuencia se enclava un cálculo, lo que explica el dolor irradiado a genitales y los síntomas miccionales irritativos cuando el cálculo está en el uréter distal."
COM[2224]="La comunicación interauricular, la comunicación interventricular y la persistencia del conducto arterioso son cardiopatías acianóticas con cortocircuito de izquierda a derecha. Parte de la sangre oxigenada vuelve a la circulación pulmonar, por lo que el flujo pulmonar supera al sistémico (Qp/Qs >1). Este hiperflujo pulmonar produce sobrecarga de volumen y, cuando es grande, insuficiencia cardiaca (taquipnea, sudoración al lactar, mala ganancia de peso). El cortocircuito de derecha a izquierda y el hipoflujo pulmonar son propios de las cardiopatías cianóticas."
EXC.update({2183:"mismo concepto ya publicado (CB-039)",2184:"mismo concepto ya publicado (PED-149)",2186:"mismo concepto ya publicado (NEF-063)",
2187:"mismo concepto que otra aceptada (2119)",2189:"clave ambigua",2190:"mismo concepto ya publicado (CIR-028)",2191:"mismo concepto ya publicado (SP-064)",
2192:"mismo concepto ya publicado (SP-083)",2195:"mismo concepto ya publicado (HEM-023)",2197:"mismo concepto ya publicado (CAR-049)",2198:"clave dudosa",
2199:"mismo concepto ya publicado (HEM-024)",2200:"mismo concepto ya publicado (PED-212)",2201:"mismo concepto que otra aceptada (2003)",
2203:"mismo concepto ya publicado (GIN-145)",2204:"mismo concepto ya publicado (PED-116)",2205:"mismo concepto ya publicado (GIN-233)",
2206:"mismo concepto ya publicado (END-027)",2210:"mismo concepto ya publicado (NEF-042)",2212:"mismo concepto ya publicado (NEF-085)",
2213:"mismo concepto ya publicado (NEU-062)",2216:"mismo concepto ya publicado (GAS-026)",2219:"clave dudosa",2220:"clave dudosa",
2222:"mismo concepto ya publicado (TRA-040)",2223:"mismo concepto ya publicado (PSI-022)",2225:"clave ambigua",2232:"clave ambigua",
2235:"mismo concepto ya publicado (PED-096)",2236:"clave ambigua",2238:"clave ambigua"})

# --- v05 ---
add((2240,CI,"Trombosis hemorroidal externa aguda: trombectomía","C"),
(2242,CA,"Insuficiencia cardiaca con hipovolemia: suspender el diurético de asa","B"),
(2243,SP,"Mortalidad materna en poblados rurales pequeños: vigilancia comunitaria","D"),
(2244,GI,"Embrión sin actividad cardiaca con cuello cerrado: aborto retenido","B"),
(2246,PE,"Escorpionismo con compromiso sistémico: faboterapia","D"),
(2248,CI,"Plastrón apendicular estable sin absceso: manejo conservador","D"),
(2249,CB,"Intoxicación por benzodiacepinas y alcohol con depresión respiratoria: proteger la vía aérea","D"),
(2256,NE,"Enfermedad renal crónica avanzada: hiperpotasemia, hiperfosfatemia, hipocalcemia y acidosis","A"),
(2257,EN,"Cetoacidosis diabética con potasio bajo: reponer potasio antes de la insulina","A"),
(2264,OF,"Glaucoma por corticoides: secundario de ángulo abierto","A"),
(2265,CB,"Fluoroquinolonas: tendinitis aquílea","B"),
(2267,CB,"Apixabán: inhibidor directo del factor Xa","C"),
(2273,RE,"Pseudogota: cristales de pirofosfato de calcio","B"),
(2275,SP,"Adolescente con abandono paterno: desestructuración familiar como determinante social","D"),
(2276,NL,"Enfermedad de Parkinson: déficit de dopamina","A"),
(2277,GI,"Ectópico tratado con metotrexato: esperar 3 meses para un nuevo embarazo","B"),
(2286,GA,"Síndrome hepatorrenal","C"),
(2288,EN,"Inhibidores de SGLT2: aumentan la glucosuria","B"),
(2291,NE,"Hipernatremia grave: deshidratación neuronal por gradiente osmótico","A"),
(2293,SP,"Mala adherencia en diabetes: programa educativo continuo","D"),
(2295,CA,"Síndrome coronario agudo sin elevación del ST: antiagregación, anticoagulación y nitratos","B"),
(2302,PE,"Lactante con VIH confirmado por PCR: TAR inmediato","A"))
OPT[2265]={"E":"Nitrofurantoína"}
COM[2240]="Dolor anal súbito tras un esfuerzo con un nódulo violáceo perianal de 1 cm: trombosis hemorroidal externa. Si el paciente consulta en las primeras 72 horas y el dolor es intenso, el tratamiento de elección es la trombectomía (escisión del trombo o de la hemorroide trombosada) con anestesia local, que alivia rápido el dolor y reduce las recurrencias. Pasadas las 72 horas se prefiere el manejo conservador (analgésicos, baños de asiento, laxantes). La escleroterapia se usa en hemorroides internas y la esfinterotomía en la fisura anal."
COM[2242]="Paciente con insuficiencia cardiaca crónica que consulta por mareo, PA baja-normal y lengua seca, sin crepitantes ni signos de congestión: está hipovolémico por exceso de diurético. El fármaco que debe suspenderse (o reducirse) es la furosemida, porque los diuréticos de asa solo alivian la congestión y no mejoran la supervivencia. El enalapril, el carvedilol y la espironolactona sí disminuyen la mortalidad y deben mantenerse si la PA, la función renal y el potasio lo permiten."
COM[2243]="Cuando la mortalidad materna se concentra en un poblado rural pequeño y disperso, lo prioritario es acercar la vigilancia a la comunidad: implementar la vigilancia comunitaria con agentes comunitarios que identifiquen y registren a las gestantes, reconozcan los signos de alarma y activen la referencia oportuna (incluida la casa de espera materna). Construir un hospital, instalar un banco de sangre o contratar especialistas en una población de menos de 300 habitantes no es factible ni costo-efectivo."
COM[2244]="Gestante de 8 semanas con sangrado y dolor, cuello cerrado y un embrión de 8 mm sin actividad cardiaca: es un aborto retenido (pérdida gestacional temprana con el producto muerto retenido en el útero). Un embrión con longitud cráneo-caudal ≥7 mm sin latido confirma la muerte embrionaria. En la amenaza de aborto el embrión tiene latido; el aborto completo ya expulsó el contenido y el séptico cursa con fiebre e infección."
COM[2246]="Niño picado por un alacrán que presenta manifestaciones sistémicas por liberación de neurotransmisores (tos y dificultad respiratoria, sialorrea, nistagmo, debilidad): es un escorpionismo moderado a grave. El tratamiento específico es la faboterapia (antiveneno o suero antialacránico) lo antes posible, junto con soporte y monitoreo en un establecimiento con capacidad resolutiva. Los antibióticos no están indicados, y la atropina puede agravar los efectos adrenérgicos."
COM[2248]="Plastrón apendicular de 7 días en tratamiento antibiótico, clínicamente estable, sin signos peritoneales y sin absceso en la ecografía: se continúa el manejo conservador (antibióticos y observación), porque operar un plastrón formado aumenta el riesgo de lesionar asas y de complicaciones. Si aparece un absceso se drena por vía percutánea, y si hay peritonitis o deterioro se opera. La apendicectomía diferida (a intervalo) se valora semanas después."
COM[2249]="Intoxicación mixta por alprazolam y alcohol con depresión del sensorio (Glasgow 10), FR de 8 y SatO₂ de 89 %: lo primero es proteger la vía aérea y asegurar la ventilación (posición, oxígeno y, si no mejora, intubación). El flumazenil no es la conducta inicial: su beneficio es limitado cuando hay alcohol u otros depresores y puede desencadenar convulsiones en consumidores crónicos de benzodiacepinas. Después se realiza el hemoglucotest y el resto del manejo de soporte."
COM[2256]="Mujer con pielonefritis a repetición, filtrado glomerular de 12 mL/min, anemia y riñones con pérdida de la diferenciación córtico-medular: enfermedad renal crónica estadio 5. El riñón no excreta potasio ni fosfato (hiperpotasemia e hiperfosfatemia), no produce calcitriol y el fosfato se une al calcio (hipocalcemia, con hiperparatiroidismo secundario), y no elimina los ácidos fijos ni regenera bicarbonato (acidosis metabólica)."
COM[2257]="Cetoacidosis diabética (glucosa 480 mg/dL, pH 7,12, HCO₃⁻ 8 mEq/L, cetonuria) con potasio de 3,2 mEq/L. Tras la hidratación inicial con suero salino, si el potasio está por debajo de 3,3 mEq/L se debe reponer potasio antes de iniciar la insulina, porque la insulina lo introduce en las células y puede provocar una hipopotasemia grave con arritmias. Cuando el potasio supera 3,3 mEq/L se inicia la insulina. El bicarbonato solo se considera si el pH es menor de 6,9."
COM[2264]="El uso prolongado de corticoides (sobre todo tópicos oftálmicos) produce un glaucoma cortisónico: los corticoides aumentan la resistencia al flujo del humor acuoso en la malla trabecular y elevan la presión intraocular con el ángulo abierto. Por tener una causa identificable es un glaucoma secundario de ángulo abierto. El primario de ángulo abierto no tiene causa conocida; el facogénico se debe al cristalino y el neovascular a la neoformación de vasos por isquemia retiniana."
COM[2267]="El apixabán es un anticoagulante oral directo que inhibe de forma directa y reversible el factor Xa (libre y unido al complejo protrombinasa), sin necesitar antitrombina; así disminuye la generación de trombina. La heparina actúa activando la antitrombina III, la warfarina inhibe la vitamina K epóxido reductasa (factores II, VII, IX y X) y el dabigatrán inhibe directamente la trombina."
COM[2273]="Monoartritis de rodilla en una adulta mayor con cristales romboidales de birrefringencia positiva débil en el líquido sinovial y condrocalcinosis radiológica: artritis aguda por cristales de pirofosfato de calcio (pseudogota). Los cristales de urato de la gota son en aguja y con birrefringencia negativa intensa. La pseudogota se asocia al envejecimiento, al hiperparatiroidismo, la hemocromatosis y la hipomagnesemia."
COM[2277]="Tras el tratamiento de un embarazo ectópico con metotrexato, se recomienda esperar al menos 3 meses antes de buscar un nuevo embarazo. El metotrexato es un antagonista del ácido fólico con potencial teratogénico, y ese intervalo permite eliminarlo del organismo y recuperar los depósitos de folato. Durante ese tiempo se usa anticoncepción y conviene suplementar ácido fólico."
COM[2286]="Cirrótico con ascitis a tensión y hemorragia digestiva que desarrolla lesión renal (creatinina 1,6 mg/dL) que no mejora pese a suspender diuréticos y expandir con albúmina, con sodio urinario muy bajo (<10 mEq/L), hiponatremia y sin shock, sepsis ni nefrotóxicos: síndrome hepatorrenal. Es una lesión funcional por vasodilatación esplácnica y vasoconstricción renal intensa. Se trata con terlipresina (o noradrenalina) más albúmina. A diferencia de la insuficiencia prerrenal, no responde a la expansión de volumen."
COM[2288]="Los inhibidores del cotransportador sodio-glucosa tipo 2 (gliflozinas, como empagliflozina o dapagliflozina) bloquean el SGLT2 del túbulo contorneado proximal, que reabsorbe la mayor parte de la glucosa filtrada. Así aumentan la excreción urinaria de glucosa (glucosuria), lo que baja la glucemia, produce diuresis osmótica y natriuresis leves y pérdida de peso. Además tienen efecto protector renal y cardiovascular."
COM[2291]="Hipernatremia grave (Na 187 mEq/L) con convulsiones y coma. El aumento brusco de la osmolaridad plasmática crea un gradiente osmótico que saca agua de las neuronas: el cerebro se deshidrata y se retrae, lo que causa disfunción neuronal y puede romper venas puente con hemorragias. Por eso aparecen letargia, convulsiones y coma. La corrección debe ser lenta (no más de 10-12 mEq/L al día) para evitar el edema cerebral."
COM[2293]="Si más del 30 % de los pacientes con diabetes tipo 2 no tienen buena adherencia al tratamiento, la intervención prioritaria es implementar un programa educativo continuo y estructurado en autocuidado: explica la enfermedad, el uso de los fármacos, la dieta, la actividad física y el automonitoreo, y está demostrado que mejora la adherencia y el control glucémico. El tratamiento domiciliario y la referencia a psiquiatría no abordan la causa del problema."
COM[2295]="Dolor torácico opresivo en reposo con episodios previos, ECG con infradesnivel del ST y marcadores aún normales: síndrome coronario agudo sin elevación del ST (angina inestable o infarto sin elevación en evolución). El manejo inicial es antiagregación plaquetaria doble (aspirina más un inhibidor P2Y12), anticoagulación (heparina) y nitroglicerina para el dolor, con monitoreo, troponinas seriadas y estratificación de riesgo. La aspirina sola es insuficiente y la prueba de esfuerzo está contraindicada en la fase aguda."
EXC.update({2241:"mismo concepto ya publicado (NEF-085)",2245:"mismo concepto ya publicado (GIN-224)",2247:"clave dudosa",
2250:"mismo concepto ya publicado (NEU-006)",2251:"mismo concepto ya publicado (TRA-014)",2252:"mismo concepto ya publicado (NRL-011)",
2253:"mismo concepto ya publicado (GIN-094)",2254:"mismo concepto ya publicado (GAS-059)",2255:"mismo concepto ya publicado (INF-031)",
2259:"clave ambigua",2270:"mismo concepto ya publicado (OFT-013)",2271:"mismo concepto ya publicado (GIN, bloque 7)",2274:"clave ambigua",
2279:"mismo concepto ya publicado (INF-053)",2282:"clave dudosa",2284:"mismo concepto ya publicado (CIR-007)",2285:"mismo concepto ya publicado (NEF-004)",
2290:"mismo concepto ya publicado (CIR-109)",2292:"mismo concepto ya publicado (PED-050)",2298:"mismo concepto ya publicado (HEM-008)",
2301:"mismo concepto ya publicado (PED-079)",2303:"mismo concepto ya publicado (CIR-110)",2304:"mismo concepto ya publicado (REU-003)"})

# --- v06 ---
add((2312,IN,"Linfogranuloma venéreo: Chlamydia trachomatis","C"),
(2315,GA,"Gradiente de albúmina suero-ascitis ≥1,1: hipertensión portal","B"),
(2319,CI,"Apendicitis con puntaje AIR alto y ecografía no concluyente: cirugía","A"),
(2321,CI,"Prueba de Trendelenburg: insuficiencia venosa","D"),
(2329,SP,"Obesidad infantil: regular la publicidad de alimentos procesados","A"),
(2337,IN,"Diarrea disentérica del adulto: ciprofloxacino","C"),
(2339,NE,"Nefropatía por contraste: diabetes y enfermedad renal previa como factores de riesgo","B"),
(2340,CB,"Déficit de MCAD: hipoglucemia en ayuno","C"),
(2343,PE,"Ictericia por lactancia materna en neonato sano: observación","D"),
(2356,GI,"Tocólisis con nifedipino: contraindicada en insuficiencia cardiaca","C"),
(2358,SP,"Técnica de control: supervisión","B"),
(2360,GA,"Coledocolitiasis: ictericia con patrón colestásico","C"),
(2365,PE,"Raquitismo carencial: rosario costal","A"),
(2367,GI,"Macrosomía y distocia de hombros: diabetes gestacional","A"))
OPT[2369]={}
COM[2312]="Varón que tuvo sexo sin protección, con una pápula genital indolora que curó sola y luego bubones inguinales dolorosos que fistulizan (a veces con el signo del surco, por afectación inguinal y femoral): linfogranuloma venéreo, causado por Chlamydia trachomatis serotipos L1, L2 y L3. Se trata con doxiciclina 100 mg cada 12 horas por 21 días. Haemophilus ducreyi (chancroide) produce úlceras dolorosas de fondo sucio con adenopatía, y la gonorrea causa uretritis purulenta."
COM[2315]="El gradiente de albúmina suero-ascitis (GASA) se calcula restando la albúmina del líquido ascítico de la sérica. Un GASA ≥1,1 g/dL indica ascitis por hipertensión portal (cirrosis, insuficiencia cardiaca, síndrome de Budd-Chiari), y un GASA <1,1 g/dL orienta a causas peritoneales como la carcinomatosis, la tuberculosis peritoneal o la pancreatitis. Con un GASA de 1,4 g/dL, lo más probable es la hipertensión portal."
COM[2319]="Mujer joven con dolor que migra de epigastrio a fosa ilíaca derecha y signo de Blumberg: sospecha de apendicitis. La escala AIR (Appendicitis Inflammatory Response) clasifica de 0-4 como riesgo bajo, 5-8 intermedio y 9-12 alto. Con un puntaje de 9 (probabilidad alta) y sin posibilidad de tomografía, se indica la cirugía (apendicectomía) sin más estudios, para no retrasar el tratamiento y evitar la perforación. La observación con antibióticos se reserva para casos de riesgo intermedio mientras se completan estudios."
COM[2321]="La prueba de Trendelenburg (de Brodie-Trendelenburg) valora la insuficiencia venosa de los miembros inferiores: con el paciente acostado y la pierna elevada se vacían las venas, se coloca un torniquete en el muslo y se pide que se ponga de pie. Si las várices se llenan rápido desde arriba al retirar el torniquete, hay insuficiencia de la válvula safenofemoral; si se llenan con el torniquete puesto, hay incompetencia de las venas perforantes. Hoy se complementa con la ecografía Doppler."
COM[2329]="Frente al aumento de la obesidad infantil en un entorno con amplio acceso a ultraprocesados, pocas áreas deportivas y escuelas sin programas de alimentación saludable, la intervención de salud pública más sostenida es actuar sobre el entorno mediante políticas: regular la publicidad y la comercialización de alimentos procesados (en el Perú, la Ley de Alimentación Saludable y los octógonos de advertencia). Los talleres, los suplementos o los controles de peso actúan sobre individuos y tienen menor alcance poblacional."
COM[2337]="Adulto con diarrea disentérica aguda (sangre y leucocitos en heces), fiebre y dolor abdominal: diarrea bacteriana invasiva, probablemente por Shigella, Campylobacter o Salmonella. Además de la rehidratación oral, está indicado un antibiótico; en el adulto se usa ciprofloxacino (o azitromicina si se sospecha resistencia o Campylobacter). La loperamida está contraindicada en la diarrea con sangre y fiebre, y el metronidazol se reserva para amebiasis o giardiasis."
COM[2339]="La nefropatía por contraste es una lesión renal aguda que aparece en las 48-72 horas siguientes a la administración de contraste yodado. Sus principales factores de riesgo son la enfermedad renal crónica previa y la diabetes (sobre todo juntas), además de la deshidratación, la insuficiencia cardiaca, la edad avanzada y los volúmenes altos de contraste. Suele producir necrosis tubular con sedimento de cilindros granulosos (no leucocitarios), y la prevención principal es la hidratación con suero salino."
COM[2340]="El déficit de acil-CoA deshidrogenasa de cadena media (MCAD) es el trastorno más frecuente de la beta-oxidación de ácidos grasos. En el ayuno, el organismo no puede usar las grasas para producir energía ni cuerpos cetónicos, por lo que agota rápidamente la glucosa y aparece una hipoglucemia hipocetósica, que puede causar convulsiones, letargia e incluso muerte súbita. El tratamiento es evitar el ayuno prolongado y dar glucosa en las descompensaciones."
COM[2343]="Neonato a término de 8 días, con lactancia materna exclusiva, activo y alimentándose bien, con bilirrubina de 12 mg/dL a predominio indirecto: ictericia asociada a la lactancia materna (ictericia por leche materna). Con esa cifra y a esa edad no alcanza el umbral de fototerapia, por lo que la conducta es la observación y seguir con la lactancia, sin suspenderla. Se controla la bilirrubina si aumenta la ictericia y se descarta colestasis si persiste más de 2-3 semanas."
COM[2356]="El nifedipino, bloqueador de canales de calcio, es un tocolítico de primera línea, pero produce vasodilatación, hipotensión, taquicardia refleja y efecto inotrópico negativo. Por eso está contraindicado en gestantes con insuficiencia cardiaca o disfunción ventricular izquierda, cardiopatías con gasto dependiente de precarga, hipotensión y cuando se usa junto con sulfato de magnesio. La diabetes no contraindica el nifedipino, pero sí los betamiméticos, que elevan la glucemia."
COM[2358]="La supervisión es la técnica de control en la que un responsable acude al establecimiento, revisa y compara lo programado con lo ejecutado, levanta un acta y, sobre todo, acompaña al equipo para analizar los problemas y proponer acciones de mejora (asistencia técnica y capacitación en servicio). El monitoreo es el seguimiento continuo de indicadores durante la ejecución, la evaluación mide resultados al final de un periodo, y la inspección verifica el cumplimiento de normas sin fines de asistencia técnica."
COM[2360]="Mujer con pancreatitis previas, dolor en hipocondrio derecho tras comida grasa, ictericia, coluria y un perfil colestásico (bilirrubina 4,2 mg/dL, fosfatasa alcalina y GGT elevadas, con transaminasas moderadas): el cálculo está en la vía biliar principal, es una coledocolitiasis. La colecistitis aguda no suele dar ictericia importante, la colangitis añade fiebre (tríada de Charcot) y la pancreatitis se diagnostica con lipasa o amilasa elevadas. Se confirma con ecografía y colangiorresonancia y se trata con CPRE."
COM[2365]="Lactante de 10 meses con lactancia materna exclusiva sin suplementos (la leche materna tiene poca vitamina D), retraso motor y ensanchamiento de las uniones condrocostales (rosario raquítico): raquitismo carencial por déficit de vitamina D. Otros signos son el craneotabes, el ensanchamiento de muñecas y el retraso en el cierre de fontanelas. En el escorbuto (déficit de vitamina C) también puede haber rosario costal, pero predominan el dolor óseo, la irritabilidad y las hemorragias de encías."
COM[2367]="La macrosomía fetal (peso mayor de 4000 g) predispone a trabajo de parto disfuncional y a distocia de hombros. La causa materna más frecuente es la diabetes gestacional: la hiperglucemia materna produce hiperinsulinismo fetal, que estimula el crecimiento y el depósito de grasa en hombros y tronco. Otros factores son la obesidad materna, la ganancia excesiva de peso y el embarazo prolongado. La preeclampsia, en cambio, se asocia a restricción del crecimiento fetal."
EXC.update({2306:"mismo concepto ya publicado (SP-068)",2308:"mismo concepto ya publicado (NEF-016)",2309:"mismo concepto ya publicado (CAR-057)",
2310:"mismo concepto ya publicado (INF-054)",2313:"mismo concepto ya publicado (CIR-014)",2314:"mismo concepto ya publicado (GAS-055)",
2316:"mismo concepto ya publicado (NRL-055)",2318:"clave ambigua",2320:"clave ambigua",2323:"clave en conflicto con REU-016",
2326:"mismo concepto ya publicado (NEU-043)",2328:"mismo concepto ya publicado (GIN-032)",2330:"mismo concepto ya publicado (GAS-017)",
2331:"mismo concepto ya publicado (PED-192)",2333:"mismo concepto ya publicado (GIN-121)",2335:"opciones sin la duración correcta",
2341:"mismo concepto ya publicado (CIR-070)",2342:"mismo concepto ya publicado (NEF-022)",2344:"mismo concepto ya publicado (GIN-096)",
2345:"mismo concepto ya publicado (GIN-177)",2346:"mismo concepto ya publicado (NEF-028)",2347:"mismo concepto ya publicado (CIR-077)",
2348:"mismo concepto ya publicado (GAS-032)",2351:"mismo concepto ya publicado (SP-044)",2363:"mismo concepto ya publicado (PED-115)",
2364:"mismo concepto ya publicado (NEU-003)",2366:"mismo concepto ya publicado (GIN-033)",2368:"mismo concepto ya publicado (INF-022)",
2369:"mismo concepto ya publicado (NEF-050)",2370:"mismo concepto ya publicado (CIR-037)",2371:"mismo concepto ya publicado (NRL-002)"})
OPT.pop(2369,None)

# --- v07 ---
add((2376,PE,"Crup leve: dexametasona oral y manejo ambulatorio","D"),
(2377,SP,"Determinante social de la salud: nivel socioeconómico bajo","D"),
(2379,CB,"Movimientos embrionarios a las 8 semanas: primeros tractos de fibras nerviosas","A"),
(2380,EN,"Síndrome de Cushing exógeno: corticoides a dosis altas","D"),
(2381,IN,"Neurocisticercosis con quistes viables: albendazol","C"),
(2382,PE,"Reanimación neonatal: cianosis persistente con buena respiración, oxígeno suplementario","A"),
(2383,SP,"Promoción de la salud: el mito de que impone estilos de vida","C"),
(2389,GI,"Escala de Bishop: cálculo del puntaje","A"),
(2406,CI,"Úlcera anal lateral: causa secundaria (tuberculosis)","D"),
(2407,SP,"Comunidad aislada: capacitar agentes comunitarios para promover la lactancia","D"),
(2411,CB,"Formulaciones de insulina: difieren en la velocidad de absorción","C"),
(2412,GA,"Hepatitis autoinmune tipo 1: ANA y anti-músculo liso","C"),
(2414,CA,"Clasificación funcional NYHA: clase II","D"),
(2416,CI,"Hernia umbilical encarcelada reducida sin complicaciones: cirugía electiva","C"),
(2418,PE,"Neumonía por varicela: aciclovir intravenoso","B"),
(2421,CI,"Colecistitis aguda complicada: cubrir gramnegativos y anaerobios","B"),
(2426,GA,"Pancreatitis aguda: activación intrapancreática del tripsinógeno","D"),
(2429,SP,"Recursos escasos en una pandemia: priorizar la mayor probabilidad de recuperación","A"),
(2435,PE,"Oxiuriasis: albendazol","C"),
(2439,PE,"Exantema súbito: exantema al ceder la fiebre","A"))

# --- v08 ---
add((2441,SP,"Niveles de investigación: aplicativo","B"),
(2443,NL,"Anticolinérgicos en el Parkinson del adulto mayor: confusión","D"),
(2446,SP,"Anemia infantil en zona rural: sesiones demostrativas de alimentación","A"),
(2451,CI,"Trauma hepático leve en el niño estable: manejo no operatorio","B"),
(2452,PE,"Displasia broncopulmonar: la menor edad gestacional es el principal factor de riesgo","A"),
(2456,GI,"Más de 5 contracciones en 10 minutos: taquisistolia","D"),
(2457,GI,"PTGO de 75 g con valores por debajo del punto de corte: sin diabetes gestacional","B"),
(2460,PE,"Grietas del pezón: técnica inadecuada de agarre","A"),
(2467,IN,"Dengue sin viajes en zona con Aedes aegypti: caso autóctono","D"),
(2468,NL,"Midriasis con ojo desviado hacia abajo y afuera: III par craneal","C"),
(2469,OF,"Cuerpo extraño corneal superficial: retiro y antibiótico tópico","B"),
(2471,SP,"Asociación entre variables categóricas: prueba de chi-cuadrado","B"),
(2474,IN,"Contacto adulto con infección tuberculosa latente: terapia preventiva","B"),
(2481,EN,"Fiebre y odinofagia con tiamazol: hemograma urgente por agranulocitosis","D"),
(2488,SP,"Falta ética reiterada de un colega: notificar al Consejo Regional","C"),
(2493,PE,"Polihidramnios: descartar atresia de esófago","C"))
COM[2380]="Mujer con redistribución de la grasa (pérdida en extremidades y acúmulo en tronco y abdomen superior), cara edematosa (facies de luna llena), acné e hirsutismo: síndrome de Cushing. La causa más frecuente es la exógena o iatrogénica, por uso prolongado de glucocorticoides a dosis altas como la dexametasona, por lo que este es el antecedente más relevante. Los anticonceptivos, los trastornos nutricionales o la obesidad familiar no producen este cuadro."
COM[2382]="Neonato que tras los pasos iniciales tiene FC >100 lpm y respira bien, pero mantiene cianosis central persistente: no necesita ventilación a presión positiva (que se indica si hay apnea, boqueo o FC <100). Lo que corresponde es colocar el oxímetro en la mano derecha y administrar oxígeno suplementario a flujo libre (o CPAP si hay dificultad respiratoria), ajustándolo según la saturación objetivo para los minutos de vida. La cianosis de las manos y los pies (acrocianosis) es normal."
COM[2389]="La escala de Bishop puntúa cinco parámetros. Dilatación: 0 cm = 0, 1-2 cm = 1, 3-4 cm = 2, ≥5 cm = 3. Borramiento: 0-30 % = 0, 40-50 % = 1, 60-70 % = 2, ≥80 % = 3. Altura de la presentación: -3 = 0, -2 = 1, -1/0 = 2, +1/+2 = 3. Consistencia: firme = 0, media = 1, blanda = 2. Posición: posterior = 0, media = 1, anterior = 2. En este caso: dilatación 2 cm (1) + borramiento 50 % (1) + altura -3 (0) + consistencia media (1) + posición media (1) = 4 puntos, un cuello desfavorable (menos de 6)."
COM[2412]="Mujer con enfermedades autoinmunes (DM1 e hipotiroidismo), hepatitis aguda con transaminasas muy elevadas e ictericia, y anticuerpos antinucleares (ANA) y anti-músculo liso (SMA) positivos a títulos altos: hepatitis autoinmune tipo 1, la forma más frecuente, típica de mujeres jóvenes y adultas. La tipo 2 se caracteriza por anticuerpos anti-LKM1 a títulos altos y predomina en niños; el título de 1/40 aquí es bajo. Se confirma con biopsia hepática y responde a corticoides y azatioprina."
COM[2414]="La clasificación funcional de la NYHA es: clase I, sin limitación de la actividad física; clase II, limitación leve, asintomático en reposo pero con síntomas (disnea, fatiga, palpitaciones) con la actividad física ordinaria; clase III, limitación marcada, síntomas con actividad menor que la ordinaria; clase IV, síntomas en reposo. Esta paciente tiene disnea y fatiga al subir al segundo piso, una actividad ordinaria, por lo que corresponde a la clase II."
COM[2426]="En la pancreatitis aguda biliar, el cálculo en la ampolla de Vater aumenta la presión en el conducto pancreático y altera la secreción. El evento clave es la activación prematura del tripsinógeno a tripsina dentro de las células acinares del propio páncreas, que a su vez activa las demás proenzimas (quimotripsinógeno, fosfolipasa, elastasa) y produce autodigestión, inflamación y necrosis. La bilis no es la que activa el tripsinógeno; normalmente la tripsina se activa en el duodeno por la enteropeptidasa."
COM[2443]="En un paciente de 77 años con Parkinson, el fármaco que con más frecuencia produce deterioro de la memoria y confusión es el biperideno, un anticolinérgico que bloquea los receptores muscarínicos centrales. Por este efecto cognitivo y por otros efectos anticolinérgicos (retención urinaria, estreñimiento, glaucoma) se evita en los adultos mayores. La levodopa y los agonistas dopaminérgicos pueden causar alucinaciones, pero la confusión y la amnesia son más típicas de los anticolinérgicos."
COM[2457]="La prueba de tolerancia oral con 75 g de glucosa entre las 24 y 28 semanas diagnostica diabetes gestacional si al menos un valor alcanza o supera los puntos de corte: ayunas ≥92 mg/dL, 1 hora ≥180 mg/dL o 2 horas ≥153 mg/dL. Esta gestante tiene 90, 160 y 140 mg/dL, todos por debajo de esos límites, por lo que la prueba es normal: es una gestante no diabética y continúa con su control prenatal habitual."
COM[2467]="Un caso confirmado de dengue en una persona que no ha viajado y vive en una zona con presencia comprobada de Aedes aegypti se clasifica como autóctono: la infección se adquirió en el mismo lugar, por transmisión local. El caso importado es el que se infectó en otra zona (con antecedente de viaje a un área con transmisión). El caso probable no tiene aún confirmación de laboratorio, y el descartado tiene resultados negativos."
COM[2469]="Soldador con una esquirla corneal superficial y agudeza visual conservada: el tratamiento es retirar el cuerpo extraño bajo anestesia tópica (con aguja o fresa, en lámpara de hendidura), incluido el anillo de óxido si lo hay, y luego aplicar antibiótico tópico para prevenir la queratitis, con control en 24 horas. El lavado solo no retira un cuerpo extraño incrustado en la córnea. Si hubiera sospecha de perforación o cuerpo extraño intraocular, no se retira y se deriva de urgencia."
COM[2481]="Paciente con enfermedad de Graves tratado con tiamazol (metimazol) que presenta fiebre alta y odinofagia: se debe sospechar agranulocitosis inducida por antitiroideos, una complicación rara pero grave que suele aparecer en los primeros meses de tratamiento. La conducta inicial es suspender el tiamazol y pedir un hemograma urgente; si los neutrófilos son menores de 500/mm³, se hospitaliza y se inician antibióticos de amplio espectro. Tratarlo como una faringitis común retrasa el diagnóstico."
EXC.update({2372:"clave dudosa",2373:"mismo concepto ya publicado (END-062)",2378:"mismo concepto ya publicado (PED-065)",
2384:"mismo concepto ya publicado (CAR-035)",2387:"mismo concepto ya publicado (CIR-057)",2390:"mismo concepto ya publicado (PED-047)",
2392:"mismo concepto ya publicado (OFT-013)",2393:"mismo concepto ya publicado (PED-067)",2394:"mismo concepto ya publicado (CIR-094)",
2398:"mismo concepto ya publicado (SP-075)",2399:"clave dudosa",2400:"mismo concepto ya publicado (NEU-033)",2403:"mismo concepto ya publicado (GAS-048)",
2404:"mismo concepto ya publicado (OFT-008)",2405:"mismo concepto ya publicado (CIR-065)",2415:"mismo concepto ya publicado (PSI-002)",
2417:"mismo concepto que otra aceptada (2105)",2419:"mismo concepto ya publicado (CIR-110)",2423:"mismo concepto ya publicado (GIN-123)",
2424:"clave en conflicto con NEU-034",2425:"mismo concepto ya publicado (REU-060)",2427:"mismo concepto ya publicado (NEF-059)",
2430:"mismo concepto ya publicado (GIN-005)",2432:"clave ambigua",2438:"clave ambigua",2440:"mismo concepto ya publicado (NEF-047)",
2444:"mismo concepto ya publicado (PED-035)",2447:"mismo concepto ya publicado (TRA-040)",2450:"clave ambigua",2455:"mismo concepto ya publicado (GIN-079)",
2458:"mismo concepto ya publicado (TRA-003)",2459:"clave dudosa",2461:"clave ambigua",2465:"mismo concepto ya publicado (GAS-017)",
2470:"mismo concepto ya publicado (CIR-071)",2473:"clave ambigua",2476:"mismo concepto ya publicado (END-019)",2478:"mismo concepto ya publicado (HEM-011)",
2480:"mismo concepto ya publicado (CIR-045)",2483:"mismo concepto ya publicado (CIR-089)",2484:"sin opción correcta",2489:"mismo concepto ya publicado (PED-126)",
2495:"mismo concepto ya publicado (PED-053)",2496:"mismo concepto ya publicado (PED-122)",2497:"mismo concepto ya publicado (CAR-006)"})

# --- limpieza tras la construcción ---
FIX8=[("profilaxis postexposición. 2","profilaxis postexposición."),("con 2 antibiótico","con antibiótico"),("respiratorios 2 leves","respiratorios leves"),
("postrado desde 2 hace","postrado desde hace"),("atraviesa la 2 placenta","atraviesa la placenta"),("cólico 2 periumbilical","cólico periumbilical"),
("retraso motor 2 y","retraso motor y"),("social que 2 contribuye","social que contribuye"),("del 2 parásito","del parásito"),
(" Aunque se ha marcado como respuesta “intolerancia transitoria”, los hallazgos clínicos refieren anafilaxia leve."," Por eso el diagnóstico es alergia a las proteínas de la leche de vaca, con manifestaciones de reacción alérgica inmediata."),
("Fisiopatológicamente en ética médica, se vulnera","Desde el punto de vista ético, se vulnera"),("Consejo Médico Regional permite","Consejo Regional del Colegio Médico permite"),
("anemia, 2 trombocitopenia","anemia, trombocitopenia"),("a repetición. 2 Examen","a repetición. Examen"),("cálculo biliar, 2 diagnosticándose","cálculo biliar, diagnosticándose")]
OPT[2421]={"D":"Anaerobios y grampositivos"}
