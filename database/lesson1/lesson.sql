-- Table: public.lesson

-- DROP TABLE public.lesson;

CREATE TABLE IF NOT EXISTS public.lesson
(
    id numeric NOT NULL,
    name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    start_time timestamp without time zone NOT NULL,
    end_time timestamp without time zone NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE public.lesson
    OWNER to postgres;

--заполнить поля данными
insert into lesson values(111, 'introduction to python', '2021-07-02 19:00:00', '2021-07-02 21:00:00');
insert into lesson values(222, 'data types', '2021-07-02 19:00:00', '2021-08-02 21:00:00');
insert into lesson values(333, 'conditions', '2021-07-02 19:00:00', '2021-09-02 21:00:00')  

select * from lesson