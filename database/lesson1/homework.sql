-- Table: public.homework

-- DROP TABLE public.homework;

CREATE TABLE IF NOT EXISTS public.homework
(
    id numeric NOT NULL,
    name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    description character varying(150) COLLATE pg_catalog."default" NOT NULL,
    start_time time without time zone NOT NULL,
    end_time time without time zone NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE public.homework
    OWNER to postgres;

--заполнить поля данными
insert into homework values(1211, 'hw1', 'first homework', '2021-09-30 16:45:06', '2021-09-29 18:05:06');
insert into homework values(1212, 'hw2', 'second homework', '2021-09-30 16:45:06', '2021-09-29 18:05:06');
insert into homework values(1213, 'hw3', 'third homework', '2021-09-30 16:45:06', '2021-09-29 18:05:06')    

select * from homework