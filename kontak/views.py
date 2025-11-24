from django.shortcuts import render

def index (request):
 context = {
  'judul'       : 'kontak',
  'isi'         : 'apa aja deh',
  'title'       : 'ini kontak',
  'banner'      : 'kontak/images/kontak.png',
  'css_global'  : 'css/css_global.css',
  'css_apps'    : [
   'blog/css/css_apps',
   'kontak/css/css_apps',
  ],
  'nav'         : [
   ('/'         , 'home'),
   ('blog/'     , 'blog'),
   ('kontak/'   , 'kontak'),
  ],
 }
 return render (request, 'kontak/index.html', context)
