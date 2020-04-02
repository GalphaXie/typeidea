from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Post, Category, Tag
from .adminforms import PostAdminForm


class CategorayOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器, 只展示当前用户分类"""

    title = "分类过滤器"
    parameter_name = 'owner_category'  # TODO ?

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "is_nav", "created_time", "post_count")
    fields = ('name', 'status', 'is_nav')
    list_filter = [CategorayOwnerFilter]

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def post_count(self, obj):
        return obj.post_set.count()  # FK关联, 一对多 obj.多类小写_set

    post_count.short_description = "文章数量"

    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_time")
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    form = PostAdminForm

    list_display = ("title", "category", "status", "created_time", "operator", "owner")  # operator 是自定义字段
    list_display_links = []  # 那些字段可以作为链接.

    list_filter = [CategorayOwnerFilter]  # 可以加双下划线的方式添加属性;这里控制的是右侧的过滤栏
    search_fields = ['title', 'category__name']  # 这里是双下划线, 可见字段可以是 FK关联的 类__字段名

    exclude = ('owner', )

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    # fields = (  # fields 还有一个作用, 就是控制编辑页面 字段的排序
    #     ("category", "title"),  # 该联合字段:　控制编辑页该字段对应的input属于一个div
    #     'desc',
    #     'status',
    #     'content',
    #     'tag'
    # )

    fieldsets = (
        ("基础配置", {
            "description": "基础配置描述",
            "fields": (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            )
        }),
        ('额外信息', {
            'classes': ('collapse', ),
            'fields': ('tag', ),
        })
    )

    filter_horizontal = ('tag', )
    # filter_vertical = ('tag', )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = "操作"

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    class Media:
        css = {
            'all': ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css', ),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )
