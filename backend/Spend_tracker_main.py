from database import insert_data, update_data, delete_data, fetch_all_spends

# Example usage
insert_data(db_name='spend', table_name='spends', category='Lover', amount=4400, currency='CZK', date='19/10/2024')
update_data(db_name='spend', table_name='spends', column_name_1='amount', value_1=9000, column_name_2='category', value_2='Car')
delete_data(db_name='spend', table_name='spends', column_name_1='category', value_1='wife', column_name_2='amount', value_2=4400)