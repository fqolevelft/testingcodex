"""initial tables and seed data"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'super_admins',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String, nullable=False)
    )
    op.create_table(
        'admins',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('super_admins.id'))
    )
    op.create_table(
        'companies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('address', sa.String, nullable=False),
        sa.Column('payday', sa.Date, nullable=False),
        sa.Column('admin_id', sa.Integer, sa.ForeignKey('admins.id'))
    )
    super_admin_table = table('super_admins', column('id', Integer), column('email', String), column('password', String))
    admin_table = table('admins', column('id', Integer), column('email', String), column('password', String), column('owner_id', Integer))
    op.bulk_insert(super_admin_table, [{'id':1,'email':'super@admin.com','password':'supersecret'}])
    op.bulk_insert(admin_table, [
        {'id':1,'email':'admin@admin.com','password':'adminpass','owner_id':1}
    ])
    company_table = table('companies', column('id', Integer), column('name', String), column('address', String), column('payday', sa.Date), column('admin_id', Integer))
    op.bulk_insert(company_table, [
        {'id':1,'name':'Company A','address':'Address A','payday':'2025-01-01','admin_id':1},
        {'id':2,'name':'Company B','address':'Address B','payday':'2025-02-01','admin_id':1},
        {'id':3,'name':'Company C','address':'Address C','payday':'2025-03-01','admin_id':1}
    ])

def downgrade():
    op.drop_table('companies')
    op.drop_table('admins')
    op.drop_table('super_admins')
