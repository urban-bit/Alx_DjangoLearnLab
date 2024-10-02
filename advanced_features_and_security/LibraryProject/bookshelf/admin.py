from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

# Create Groups
editors, _ = Group.objects.get_or_create(name='Editors')
viewers, _ = Group.objects.get_or_create(name='Viewers')
admins, _ = Group.objects.get_or_create(name='Admins')

# Get permissions
content_type = ContentType.objects.get_for_model(Book)
can_view = Permission.objects.get(codename='can_view', content_type=content_type)
can_create = Permission.objects.get(codename='can_create', content_type=content_type)
can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

# Assign permissions to groups
editors.permissions.add(can_create, can_edit)
viewers.permissions.add(can_view)
admins.permissions.add(can_view, can_create, can_edit, can_delete)
