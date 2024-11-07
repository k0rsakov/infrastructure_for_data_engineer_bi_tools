from connectors_to_databases import PostgreSQL

pg = PostgreSQL(
    database="bi",
)

pg.execute_script(
    """
    COMMENT ON TABLE public.users IS 'Таблица текущих пользователей';

    COMMENT ON COLUMN public.users.id IS 'Уникальный id пользователя';
    COMMENT ON COLUMN public.users.created_at IS 'Дата регистрации';
    COMMENT ON COLUMN public.users.updated_at IS 'Дата обновления информации по пользователю';
    COMMENT ON COLUMN public.users.first_name IS 'Имя';
    COMMENT ON COLUMN public.users.last_name IS 'Фамилия';
    COMMENT ON COLUMN public.users.middle_name IS 'Отчество';
    COMMENT ON COLUMN public.users.birthday IS 'Дата рождения';
    COMMENT ON COLUMN public.users.email IS 'e-mail';
    COMMENT ON COLUMN public.users.city IS 'Город последней покупки';
    """,
)
