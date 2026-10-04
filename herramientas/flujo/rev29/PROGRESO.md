# Entrega 2 (flujogramas 501-1000 de algoritmos.js)
Lista en `rev29/entrega2.json`; fichas en `rev29/tNN.txt` (25 c/u). Contenido en `content29a.py` (t00), `content29b.py` (t01)…
Construir: `python3 build28.py <out> $(ids)` → `node check27.cjs <out>/flujogramas <out>/png`; franjas: `python3 rev28/franjas.py <out> hoja.png`.
Imágenes: Commons (`img/cm.py`, `img/wm.py`), recortes y montajes en `img/prep29.py`; propias: `img/ecg29.py` (ECG) y `img/frotis29.py` (frotis).

| Tanda | Archivo | Estado |
|---|---|---|
| t00 | content29a.py | hecha, 0 problemas; 13 con imagen (volvulo_rx, atelectasia_rx, vivax_troz, hiperseg2, lmc_frotis, falcip, romana+triatoma, placenta_previa, epistaxis, pilonidal, xantoma+tubo; reutiliza uip_tc, ferropenia) |
| t01 | content29b.py | hecha, 0 problemas; 14 con imagen (bronquiolitis_rx, meconio_rx, mallory, dib_hernia_crural [dibujo propio], ecg_tep [ECG propio], retinopatia, mantoux, toxo_rm, giardia, atresia_rx, janeway, periamig, ascitis, cilindro_granuloso) |
| t02 | content29c.py | hecha, 0 problemas; 17 con imagen (nuevas: polipo, vcs_venas, endometrioma, urt_colin, apendicitis_eco, bridas_rx, versicolor, lcn, manguito [rótulos en español], cara_mp; propias: ecg_hipermag, ecg_taponamiento, ecg_extrasistole, dib_nomograma_paracetamol; reutiliza chancro, cprm_coledoco, piloro) |
| t03 | content29d.py | hecha, 0 problemas; 13 con imagen (ictericia, strongy, lazo, russell, midriasis, saco, pancreatitis_tc, zoster+tzanck, ulcera_endo; propias: dib_balanza_ulcera, dib_hernia_inguinal; reutiliza apendicitis_eco, rx_neumotorax_grande). Precisiones: INF-038 en heces se ven larvas, no huevos; PSI-016 con 3 meses el DSM-5-TR lo llama esquizofreniforme |
| t04 | content29e.py | hecha, 0 problemas; 13 con imagen (papiledema, tobillo [rótulos en español], oxalato, hidradenitis, oxiuro, cilindro_hematico; propia: dib_coartacion; reutiliza ectopico_tubario, janeway, meningococo, pancreatitis_tc) |
| t05 | content29f.py | hecha, 0 problemas; 14 con imagen (esporotricosis, diu, tvp, feo_tc, lla_real, gottron; propias: ecg_fv, dib_canal_endemico; reutiliza hsa_tc, glioblastoma, wernicke_flair) |
| t06 | content29g.py | hecha, 0 problemas; 8 con imagen (graf, hematoma_oreja, petequias, ishihara, chagas_ecg_rx [ECG propio + megaesófago]; propia: dib_kramer; reutiliza ictericia, mola) |
| t07 | content29h.py | hecha, 0 problemas; 12 con imagen (gonococo, kaposi, ferruginoso, colera, hidronefrosis, bota, hidrocefalia; propias: dib_tarjeta_heces, ecg_qt_tdp, ecg_iam_al) |
| t08 | content29i.py | hecha, 0 problemas; 11 con imagen (strep_petequias, tb_miliar, pavlik; propias: dib_cobb, dib_banera; reutiliza ncc_tc, ascitis, hsa_tc, papiledema, dib_hernia_inguinal, ictericia) |
| t09 | content29j.py | hecha, 0 problemas; 15 con imagen (lepto, cprm, fijador, pliegue, megalo_mont [foto + frotis propio], sarna_surco, otitis_ext, acne, conjuntivitis; propias: dib_pupilas, dib_triangulo_femoral; reutiliza ecg_taponamiento, aedes). Precisiones: PED-108, GAS-039, GAS-040, REU-029 |
| t10 | content29k.py | hecha, 0 problemas; 12 con imagen (collarin [dibujo CC0], pca, psoriasis_mont, paracentesis, hiv_eco, varices_wale, sarampion_mont; reutiliza pancreatitis_tc, neumonia_lm, gottron, dib_hernia_crural) |
| t12 | content29m.py | hecha, 0 problemas; 10 con imagen (metastasis_rm, escarotomia, graves_ojos, pie_zambo, onfalitis, lupus_malar; reutiliza dib_tarjeta_heces, papiledema, dib_pupilas, hidronefrosis). Falta colposcopía (Commons 429, se reintenta) |
| t11 | content29l.py | hecha, 0 problemas; 13 con imagen (alz_rm, fast_morison, otitis_cronica, livedo, hic_tc, emh_rx; propias: dib_craneo_rn, dib_derrame, dib_cerumen; reutiliza ecg_fv, ecg_fa) |
| t13 | content29n.py | hecha, 0 problemas; 8 con imagen (celulas_clave [rótulos en inglés borrados], escrofula, geniogloso; propia: dib_dengue_pruebas; reutiliza janeway) |
| t14 | content29o.py | hecha, 0 problemas; 7 con imagen (panal_candida, hipema, pelagra [manos]; propia: dib_regla9; reutiliza pcp_rx, ectopico_tubario) |
| t15 | content29p.py | hecha, 0 problemas; 2 con imagen (propia: ecg_fa_rapida; reutiliza ecg_tep). Commons con límite 429: pendientes escafoides y tórax inestable |
| t16 | content29q.py | hecha, 0 problemas; 3 con imagen (propias: dib_posturas, ecg_pericarditis; reutiliza vivax_troz) |
| t17 | content29r.py | hecha, 0 problemas; 5 con imagen (propias: dib_formula_obstetrica, dib_partograma; reutiliza emh_rx, ecg_fv, petequias) |
| t18 | content29s.py | hecha, 0 problemas; 4 con imagen (propias: dib_piel_quemadura, dib_placenta; Commons: varicela; reutiliza rx_neumotorax_grande). Además REU-034 (t13) recibió foto de liendres |
| t19 | content29t.py | hecha, 0 problemas; 11 con imagen (Commons: crup_campanario, acantosis, cec_labio; propias: dib_peroneo, dib_bakri, dib_pie_plano, ecg_qt_largo; reutiliza neumonia_lm, dib_derrame, dib_piel_quemadura) |
