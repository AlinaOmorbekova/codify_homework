CREATE TABLE IF NOT EXISTS public.student
(
    id numeric(100,0) NOT NULL,
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    middle_name character varying(100) COLLATE pg_catalog."default",
    email character varying(100) COLLATE pg_catalog."default" NOT NULL,
    birth_date date NOT NULL,
    registration_date date,
    my_group character varying(150) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE public.student
    OWNER to postgres;
-- заполнить таблицу данными    
INSERT INTO student VALUES(1111, 'alina', 'omorbekova', 'omorbekovna', 'alina1gmail.com', '1999-07-20');
INSERT INTO student VALUES(1112, 'alina1', 'omorbekova1', 'omorbekovna', 'alina2gmail.com', '1999-07-20');
INSERT INTO student VALUES(1113, 'alina2', 'omorbekova2', 'omorbekovna', 'alina3gmail.com', '1999-07-20');
INSERT INTO student VALUES(1114, 'alina3', 'omorbekova3', 'omorbekovna', 'alina4gmail.com', '1999-07-20');
INSERT INTO student VALUES(1115, 'alina4', 'omorbekova4', 'omorbekovna', 'alina5gmail.com', '1999-07-20');
INSERT INTO student VALUES(1116, 'alina5', 'omorbekova5', 'omorbekovna', 'alina6gmail.com', '1999-07-20');
INSERT INTO student VALUES(1117, 'alina6', 'omorbekova6', 'omorbekovna', 'alina7gmail.com', '1999-07-20');
INSERT INTO student VALUES(1118, 'alina7', 'omorbekova7', 'omorbekovna', 'alina8gmail.com', '1999-07-20');
INSERT INTO student VALUES(1119, 'alina8', 'omorbekova8', 'omorbekovna', 'alina9gmail.com', '1999-07-20');
INSERT INTO student VALUES(1120, 'alina9', 'omorbekova9', 'omorbekovna', 'alina10gmail.com', '1999-07-20')
-- добавить поле "дата регистрации" и "группа" с помощью ALTER
ALTER TABLE student
ADD COLUMN registration_date date;
ADD COLUMN my_group character varying(150);
-- добавить информацию в поле "дата регистрации" и "группа"
UPDATE student
SET registration_date = '2021-09-29'
SET my_group = 'python-07'
--изменить на NOT NULL
ALTER TABLE student
ALTER COLUMN registration_date SET NOT NULL;
ALTER COLUMN my_group SET NOT NULL;

select * from student;