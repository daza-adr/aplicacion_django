from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliente',
            new_name='Estudiante',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='tipo_documento',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='whatsapp',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='asistencia',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='direccion',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
