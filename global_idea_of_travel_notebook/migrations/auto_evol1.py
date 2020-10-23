
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('global_idea_of_travel_notebook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='author',
            new_name='owner',
        ),
    ]
