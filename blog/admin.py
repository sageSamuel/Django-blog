from django.contrib import admin
from .models import Comment, Post

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
    



@admin.register(Post)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'slug',
                    'author', 
                    'publish',
                    'status'
                    ]
    list_filter = ['status', 'created', 'publish', 'author'] #this adds a filter sidebar
    search_fields = ['title', 'body'] #this adds a search box
    prepopulated_fields = {'slug': ('title',)} #this auto populates the slug field based on the title   
    raw_id_fields = ['author'] #this changes the author field to a raw id field
    date_hierarchy = 'publish' #this adds a date based drill down navigation by publish date
    ordering = ['status', 'publish'] #this orders the posts by status and publish date  
    show_facets = admin.ShowFacets.ALWAYS #this shows the filter sidebar by default
    
    
    
    
