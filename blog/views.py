from django.shortcuts import render

def index (request):
 context = {
  'judul'       : 'blog',
  'isi'         : 'apa aja deh',
  'title'       : 'ini blog',
  'banner'      : 'blog/images/blog.png',
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
 return render (request, 'blog/index.html', context)