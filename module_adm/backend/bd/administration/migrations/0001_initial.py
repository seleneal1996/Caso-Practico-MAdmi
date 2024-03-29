# Generated by Django 3.2.6 on 2024-03-12 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id_colaborador', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('dni', models.CharField(max_length=15)),
                ('estado', models.CharField(choices=[('activo', 'activo'), ('inactivo', 'inactivo')], default='activo', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('eps', models.BooleanField()),
                ('insurance', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('administrator', 'administrator'), ('user', 'user')], default='user', max_length=15)),
                ('id_collaborator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.collaborator')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday'), ('saturday', 'saturday'), ('sunday', 'sunday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('id_collaborator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.collaborator')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=50)),
                ('id_collaborator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.collaborator')),
                ('id_contract_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.contracttype')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(choices=[('phone', 'phone'), ('email', 'email')], max_length=10)),
                ('contact_detail', models.CharField(max_length=255)),
                ('id_collaborator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.collaborator')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.contract')),
                ('id_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.schedule')),
            ],
        ),
    ]
