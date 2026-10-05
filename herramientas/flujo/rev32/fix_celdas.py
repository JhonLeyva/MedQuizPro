"""Rellena las celdas sin imagen (pedido del 5-oct): cada celda de la cuadrícula lleva su foto o dibujo."""
import re, glob
W = 'fondo="#ffffff"'
TX = lambda pat: f'D(lambda s, x, y: I.torax_rx(s, x, y, "{pat}", sc=0.9), 270, 252)'
CELDAS = {
 "INF-075": ({"Herpes simple": 'P("herpes_esof.jpg", 380, 214)', "Úlcera idiopática (aftosa)": f'PA("dib_ulcera_idiopatica.jpg", 300, [], {W})'},
             " · Herpes: Mwengela et al. · Cureus 2026 · PMC13283467 · CC BY 4.0 · Úlcera: esquema MedQuizPro"),
 "REU-040": ({"Queratosis seborreica": 'P("qseb.jpg", 360, 196)'}, " · Queratosis: Lubis y Putra · Front Med 2026 · PMC13587691 · CC BY 4.0"),
 "OFT-033": ({"Uveítis anterior": 'P("hipopion.jpg", 330, 318)', "Queratitis": 'P("queratitis.jpg", 360, 291)'},
             " · Hipopion: Ajabshir et al. · Cureus 2024 · PMC11707805 · Queratitis: Gardeli et al. · Cureus 2026 · PMC13552464 · CC BY 4.0"),
 "PED-144": ({"Taquipnea transitoria": TX("edema"), "Neumonía neonatal": TX("consolidacion")}, " · Abajo: esquemas MedQuizPro"),
 "CB-056": ({"Serpiente (ofidismo)": 'P("bothrops.jpg", 380, 285)'}, " · Bothrops: Pedigone et al. · Rev Soc Bras Med Trop 2026 · PMC13379231 · CC BY 4.0"),
 "CIR-089": ({"Hemotórax masivo": 'P("hemotorax_a.jpg", 300, 299)', "Tórax inestable": f'P("torax_inestable.jpg", 330, 248, [], {W})'},
             " · Hemotórax: Abdalrahman et al. · PMC13536977 · CC BY 4.0 · Tórax inestable: Baedr-9439 (CC0)"),
 "PED-149": ({"Primaria (niño)": 'P("ghon_rx.jpg", 261, 288)', "Pleural": 'P("tb_pleural_rx.jpg", 220, 211)'},
             " · Ghon y derrame: Basem Abbas Al Ubaidi (CC BY 4.0)"),
 "REU-047": ({"Traumatismo": 'P("hematoma_subungueal.jpg", 330, 272)'}, " · Hematoma: Callaleo (CC BY-SA 4.0)"),
 "GIN-155": ({"Antecedente típico": 'P("cuello_dilatado_eco.jpg", 360, 240)', "Tratamiento": 'P("cerclaje_eco.jpg", 360, 247)'},
             " · Abajo: Shir et al. · Case Rep Obstet Gynecol 2026 · PMC13494658 · CC BY 4.0"),
 "PED-160": ({"Uraco permeable": f'PA("dib_uraco.jpg", 300, [], {W})', "Conducto onfalomesentérico": f'PA("dib_onfalomesenterico.jpg", 300, [], {W})'},
             " · Abajo: esquemas MedQuizPro"),
 "OFT-039": ({"Otomicosis": 'P("otomicosis.jpg", 300, 424)'}, " · Otomicosis: Mohammad2018 (CC BY-SA 4.0)"),
 "INF-090": ({"Chlamydia trachomatis": f'PA("dib_gram_pmn.jpg", 300, [], {W})', "Mycoplasma genitalium": f'PA("dib_naat.jpg", 300, [], {W})',
              "Trichomonas": 'P("trico.jpg", 420, 350)'}, " · Tricomonas: CDC/PHIL (dominio público) · Esquemas MedQuizPro"),
 "CB-070": ({"B1 · Tiamina (beriberi)": f'PA("dib_beriberi.jpg", 330, [], {W})', "B2 · Riboflavina": 'P("queilitis.jpg", 360, 170)',
             "B12 · Cobalamina": f'P("hiperseg2.jpg", 300, 251, [], {W})'},
            " · Queilitis: Matthew Ferguson 57 (CC BY-SA 3.0) · Neutrófilo: Ed Uthman (CC BY 2.0) · Beriberi: esquema MedQuizPro"),
 "CB-072": ({"Metanol": 'P("metanol_tc.jpg", 300, 417)',
             "Cetoacidosis diabética": 'D(lambda s, x, y: I.tira_orina(s, x, y, [("Glucosa", "#7c2d12", "+++", True), ("Cetonas", "#7e22ce", "+++", True), ("pH", "#f59e0b", "5", False)], sc=1.0), 230, 120)',
             "Acidosis láctica (metformina)": 'P("metformina.jpg", 330, 140)'},
            " · TC: Sandhu et al. · Case Rep Radiol 2026 · PMC13527635 · CC BY 4.0 · Metformina: User:Ash (dominio público)"),
 "INF-092": ({"Uncinarias": 'P("uncinaria.jpg", 300, 195)', "Ascaris": 'P("ascaris_huevo.jpg", 330, 225)'},
             " · Uncinaria: Jiang y Zhu · Rev Inst Med Trop 2026 · PMC13450911 · CC BY 4.0 · Ascaris: CDC/M. Melvin (dominio público)"),
 "CAR-064": ({"Actividad eléctrica sin pulso": f'P("ecg_normal_ii.jpg", 450, 90, [], credito="Trazado de enseñanza MedQuizPro", {W})'}, ""),
 "INF-095": ({"Celulitis": 'P("celulitis.jpg", 380, 309)', "Erisipela": 'P("erisipela.jpg", 360, 254)', "Fascitis necrosante": 'P("fascitis.jpg", 360, 370)'},
             " · Celulitis: Suenaert et al. · Cureus 2026 · PMC13564028 · Fascitis: Septiawan et al. · J Surg Case Rep 2026 · PMC13589848 · CC BY 4.0 · Erisipela: Grook Da Oger (CC BY-SA 3.0)"),
 "INF-098": ({"Mycoplasma / Legionella": 'D(lambda s, x, y: I.torax_rx(s, x, y, "intersticial", sc=0.5), 150, 140)'}, ""),
 "NEF-082": ({"Prerrenal": f'PA("dib_prerrenal.jpg", 330, [], {W})', "Renal (intrínseca)": f'P("cilindro_granuloso.jpg", 330, 194, [], {W})',
              "Pista de este caso": f'PA("dib_globo_vesical.jpg", 300, [], {W})'}, " · Cilindro: Mohsenin V. (CC BY 4.0) · Esquemas MedQuizPro"),
}
files = {f: open(f).read() for f in sorted(glob.glob("content30[a-t].py"))}
for i, (cel, cred) in CELDAS.items():
    f = [f for f, s in files.items() if re.search(r'^S\("[a-z_]+", "%s"' % i, s, re.M)][0]
    s = files[f]
    a = re.search(r'^S\("[a-z_]+", "%s"' % i, s, re.M).start()
    m = re.compile(r'^(# |S\()', re.M).search(s, a + 5); b = m.start() if m else len(s)
    blk = s[a:b]
    for name, img in cel.items():
        rx = re.compile(r'(\("%s", \[[^\]]*\], )None' % re.escape(name))
        assert rx.search(blk), (i, name)
        blk = rx.sub(lambda mm: mm.group(1) + img, blk, count=1)
    if cred:
        mm = re.search(r'credito=("[^"]*"|[A-Z_]+)( \+ [^\n]*?)?,\n', blk)
        assert mm, i
        blk = blk[:mm.end() - 2] + ' + "' + cred + '"' + blk[mm.end() - 2:]
    files[f] = s[:a] + blk + s[b:]
for f, s in files.items():
    open(f, "w").write(s)
# PED-142: estadios 1 y 4-5 con foto
f = "content30a.py"; s = open(f).read()
s = s.replace('"Línea blanca plana entre la retina con vasos y la que no tiene.", None, False)', '"Línea blanca plana entre la retina con vasos y la que no tiene.", P("rop_b.jpg", 246, 184), False)')
s = s.replace('"4: parcial · 5: total (ceguera).", None, False)', '"4: parcial · 5: total (ceguera).", P("rop_e5.jpg", 330, 334), False)')
s = s.replace('credito=PMC_ROP + " · " + PMC_PLUS),', 'credito=PMC_ROP + " · " + PMC_PLUS + " · Estadio 5: Singh et al. · Cureus 2026 · PMC13559123 · CC BY 4.0"),')
open(f, "w").write(s)
print("ok")
