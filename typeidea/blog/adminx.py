import xadmin
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry
from xadmin.filters import RelatedFieldListFilter, manager
from xadmin.layout import Row, Fieldset, Container

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from typeidea.base_admin import BaseOwnerAdmin


class CategorayOwnerFilter(RelatedFieldListFilter):
    """自定义过滤器, 只展示当前用户分类"""

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        # 重新获取 lookup_choices, 根据 owner 过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list("id", "name")


class PostInline:  # StackedInline 样式不同
    form_layout = (
        Container(
            Row('title', 'desc'),
        )
    )
    extra = 1  # 控制额外多几个
    model = Post


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ("name", "status", "is_nav", "created_time", "post_count", "owner")
    fields = ('name', 'status', 'is_nav')

    # inlines = [PostInline, ]  # 这里只是为了演示用法， 具体这里用不到，注释掉。

    def post_count(self, obj):
        return obj.post_set.count()  # FK关联, 一对多 obj.多类小写_set

    post_count.short_description = "文章数量"


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ("name", "status", "created_time")
    fields = ('name', 'status')


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):

    form = PostAdminForm

    list_display = ("title", "category", "status", "created_time", "operator")  # operator 是自定义字段
    list_display_links = []  # 那些字段可以作为链接.

    list_filter = ['category']  # 可以加双下划线的方式添加属性;这里控制的是右侧的过滤栏
    search_fields = ['title', 'category__name']  # 这里是双下划线, 可见字段可以是 FK关联的 类__字段名

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    form_layout = (
        Fieldset(
            "基础信息",
            Row('title', 'category'),
            'status',
            'tag'
        ),
        Fieldset(
            "内容信息",
            'desc',
            'content',
        )
    )

    filter_horizontal = ('tag', )
    # filter_vertical = ('tag', )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            # reverse('xadmin:blog_post_change', args=(obj.id,))  # 方法一
            self.model_admin_url('change', obj.id)

        )

    operator.short_description = "操作"

    @property
    def media(self):
        # xadmin 基于 Bootstrap， 引入会导致页面样式冲突， 这里仅演示
        media = super().media
        media.add_js(["https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js"])
        media.add_css({
            "all": ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css")
        })


@xadmin.sites.register(LogEntry)
class LogEntryAdmin:
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']


manager.register(CategorayOwnerFilter, take_priority=True)
