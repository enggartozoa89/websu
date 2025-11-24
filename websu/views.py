from django.shortcuts import render

def index (request):
 context = {
  'judul'       : 'home',
  'isi'         : 'apa aja deh',
  'title'       : 'ini home',
  'banner'      : 'images/beranda.png',
  'css_global'  : 'css/css_global.css',
  'css_apps'    : [
   'blog/css/css_apps',
   'kontak/css/css_apps',
  ],
  'nav'         : [
   ('/'         , 'home'),
   ('blog/'     , 'blog'),
   ('kontak/'   , 'kontak'),
  ] ,
 }
 return render (request, 'index.html', context)