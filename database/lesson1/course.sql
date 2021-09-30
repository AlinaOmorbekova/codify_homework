CREATE TABLE IF NOT EXISTS public.course
(
    id numeric NOT NULL,
    name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    start_date date NOT NULL,
    end_date date,
    price double precision
)

TABLESPACE pg_default;

ALTER TABLE public.course
    OWNER to postgres;


--заполнить данными
insert into course values(01, 'python', '2021-07-02', '2021-12-31', 60000);
insert into course values(02, 'java', '2021-08-02', '2022-01-31', 100000);
insert into course values(03, 'pm', '2021-09-02', '2022-03-31', 50000)

--добавить поле "цена"
alter table course
add column price numeric;

--заполнить данными поле Цена
update course
set price = 10000

--NOT NULL

alter table course
alter column price
SET NOT NULL;

select * from course
