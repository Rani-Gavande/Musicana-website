from django.contrib import admin
from Muser.models import SignUp,TRENDINGSong,Artist,ArtistSong,Album,AlbumSong ,PopularSong,MarathiSong,TamilSong
# Register your models here.

admin.site.register(SignUp)
admin.site.register(Artist)
admin.site.register(ArtistSong)
admin.site.register(TRENDINGSong)
admin.site.register(PopularSong)
admin.site.register(Album)
admin.site.register(AlbumSong)
admin.site.register(MarathiSong)
admin.site.register(TamilSong)
