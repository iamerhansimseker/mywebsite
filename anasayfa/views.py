from django.shortcuts import render

def merhaba(request):
    return render(request, 'anasayfa/merhaba.html')

def hello(request):
    return render(request, 'anasayfa/hello.html')

def hakkimda(request):
    return render(request, 'anasayfa/hakkimda.html')  # 👈 Hakkımda sayfası

def about_me(request):
    return render(request, 'anasayfa/about_me.html')  # 👈 Hakkımda sayfası

def neler_yaptim(request):
    return render(request, 'anasayfa/neler_yaptim.html')  # 👈 Yeni: Neler Yaptım? sayfası

def what_I_did(request):
    return render(request, 'anasayfa/what_I_did.html')

def deneyimlerim(request):
    return render(request, 'anasayfa/deneyimlerim.html')

def experiences(request):
    return render(request, 'anasayfa/experiences.html')

def projelerim(request):
    return render(request, 'anasayfa/projelerim.html')

def projects(request):
    return render(request, 'anasayfa/projects.html')

def proje_tez(request):
    return render(request,'anasayfa/proje_tez.html')

def tez_en(request):
    return render(request,'anasayfa/tez_en.html')

def video_tez(request):
    return render(request, 'anasayfa/video_tez.html')

def video_tez_en(request):
    return render(request, 'anasayfa/video_tez_en.html')

def proje_staj(request):
    return render(request, 'anasayfa/proje_staj.html')

def staj_en(request):
    return render(request, 'anasayfa/staj_en.html')

def proje_staj_genis(request):
    return render(request, 'anasayfa/tedas_genis.html')

def tedas_ext(request):
    return render(request, 'anasayfa/tedas_ext.html')

def proje_staj_sunum(request):
    return render(request,'anasayfa/tedas_sunum.html')

def tedas_pre(request):
    return render(request,'anasayfa/tedas_pre.html')

def proje_sasamakro(request):
    return render(request,'anasayfa/sasamakro_tr.html')

def sasamakro_en(request):
    return render(request,'anasayfa/sasamakro_en.html')

def proje_veri(request):
    return render(request,'anasayfa/veri_bilimi_tr.html')

def veri_en(request):
    return render(request,'anasayfa/veri_en.html')

def proje_network(request):
    return render(request,'anasayfa/network_tr.html')

def network_en(request):
    return render(request,'anasayfa/network_en.html')

def proje_project_planning(request):
    return render(request,'anasayfa/project_planning_tr.html')

def project_planning_en(request):
    return render(request,'anasayfa/project_planning_en.html')

def proje_regresyon(request):
    return render(request,'anasayfa/regresyon_tr.html')

def reg_en(request):
    return render(request,'anasayfa/reg_en.html')
