import sql_manager


def main():
    sql_manager.drop_clients_table()
    sql_manager.create_clients_table()


if __name__ == '__main__':
    main()
