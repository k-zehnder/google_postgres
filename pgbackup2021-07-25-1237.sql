PGDMP     9    %                y           work #   12.7 (Ubuntu 12.7-0ubuntu0.20.04.1) #   12.7 (Ubuntu 12.7-0ubuntu0.20.04.1)     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    35996    work    DATABASE     v   CREATE DATABASE work WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE work;
                zelda    false            �            1259    36014 
   User_calls    TABLE     �  CREATE TABLE public."User_calls" (
    "Phone Number" text,
    gender text,
    dob text,
    weight text,
    height text,
    activity text,
    hobby text,
    "time zone" text,
    "call time" text,
    "emergency phone" text,
    "emergency name" text,
    username text,
    "datetime added" text,
    friend text,
    operator text,
    type text,
    "CreatedUTC" timestamp without time zone
);
     DROP TABLE public."User_calls";
       public         heap    zelda    false            �            1259    36020    User_existing    TABLE     �  CREATE TABLE public."User_existing" (
    "Phone Number" text,
    gender text,
    dob text,
    weight text,
    height text,
    activity text,
    hobby text,
    "time zone" text,
    "call time" text,
    "emergency phone" text,
    "emergency name" text,
    username text,
    "datetime added" text,
    friend text,
    operator text,
    type text,
    "CreatedUTC" timestamp without time zone
);
 #   DROP TABLE public."User_existing";
       public         heap    zelda    false            �            1259    36026 	   User_time    TABLE     �   CREATE TABLE public."User_time" (
    "Username" text,
    "Timezone" text,
    "UTC start" text,
    "UTC end" text,
    "Number" bigint,
    "CreatedUTC" timestamp without time zone
);
    DROP TABLE public."User_time";
       public         heap    zelda    false            �            1259    35997    backupdb_table    TABLE     h  CREATE TABLE public.backupdb_table (
    "Phone Number" text,
    gender text,
    dob text,
    weight text,
    height text,
    activity text,
    hobby text,
    "time zone" text,
    "call time" text,
    "emergency phone" text,
    "emergency name" text,
    username text,
    "datetime added" text,
    friend text,
    operator text,
    type text
);
 "   DROP TABLE public.backupdb_table;
       public         heap    zelda    false            �            1259    36003    students    TABLE     �   CREATE TABLE public.students (
    id integer NOT NULL,
    fname character varying(40),
    lname character varying(40),
    pet character varying(40)
);
    DROP TABLE public.students;
       public         heap    zelda    false            �            1259    36006    students_id_seq    SEQUENCE     �   CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.students_id_seq;
       public          zelda    false    203            �           0    0    students_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;
          public          zelda    false    204            "           2604    36013    students id    DEFAULT     j   ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);
 :   ALTER TABLE public.students ALTER COLUMN id DROP DEFAULT;
       public          zelda    false    204    203            �          0    36014 
   User_calls 
   TABLE DATA           �   COPY public."User_calls" ("Phone Number", gender, dob, weight, height, activity, hobby, "time zone", "call time", "emergency phone", "emergency name", username, "datetime added", friend, operator, type, "CreatedUTC") FROM stdin;
    public          zelda    false    205   �       �          0    36020    User_existing 
   TABLE DATA           �   COPY public."User_existing" ("Phone Number", gender, dob, weight, height, activity, hobby, "time zone", "call time", "emergency phone", "emergency name", username, "datetime added", friend, operator, type, "CreatedUTC") FROM stdin;
    public          zelda    false    206   �       �          0    36026 	   User_time 
   TABLE DATA           m   COPY public."User_time" ("Username", "Timezone", "UTC start", "UTC end", "Number", "CreatedUTC") FROM stdin;
    public          zelda    false    207   \       �          0    35997    backupdb_table 
   TABLE DATA           �   COPY public.backupdb_table ("Phone Number", gender, dob, weight, height, activity, hobby, "time zone", "call time", "emergency phone", "emergency name", username, "datetime added", friend, operator, type) FROM stdin;
    public          zelda    false    202          �          0    36003    students 
   TABLE DATA           9   COPY public.students (id, fname, lname, pet) FROM stdin;
    public          zelda    false    203   �        �           0    0    students_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.students_id_seq', 11, true);
          public          zelda    false    204            $           2606    36010    students students_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.students DROP CONSTRAINT students_pkey;
       public            zelda    false    203            �   �  x���Mo1���X�L������T*= �(��UX`�$��)~=c*���M�-�d����;_^w��6��ݻ_�λ���6��ֻL�JVYs��g���U[�k�?��ݾ�FG@�]Qh ������p⚍s���sۜ�?��w��޴��~�6W�a�{�^w���0\�ݍwo�u��_7�~k^�ö	�~h���hN����Mu�<}��Z�4�L�9)<x>�S2�9Ƥ���o�͏��w�eEܠ�"�%9���7P91L W��b3K�jBB�2��	�N!&�Jx��g q؀Y�%d("��g�z"��{7�BC����q�SZ3���'�Wc�Τ��
���k],�Z��1M��];>��P���� �B���*����V��H�XYe�|�w��A8C�tZ�g��w��:���(=h��fQBP�	�|6�T��R�Q����X�
�~�	u�I;��Ϭ	��$�)�qaE+Ƃ�! ?'���0�2���iyw��Cxa^��T��c�Yu��?�� P�k���<j,�B�Ů�Y�ds�h�P��5I�E1X�H�y �� �ha���!�Hy�T)Ve�J�_B)�@0����b�|Tɢ��J�Pr�eNެ	�e�;d<��dar5^�>{q�!�-�������p!�Dr>����?Q�
Z      �   �  x���Mo�0��zf������T*= �(��h	uw��-~=c*�TJ����l����;_���v��w\��ݯv����_w�O��~�]&Y���9���M��٪-ֵ����n�u�# \��(4��s	����5�.���9��k�ٽio���m����y����>7�a���޶��K�n���^^�ö	�~h���hN����Mu�<}��Z�4�L�9)<x>�S2�9Ƥ���o�͏��w�eEܠ�"�%9���7P91L W��b3K�jBB�2��	�N!&�Jx��g q؀Y��B���O��ꉬ���8�"X x$V�ǡOi�h�c�`_�];��;l*�
�W�u�kI�4�^v���BA.^Ђ�J"���Zq�"�<+�̞o�n�?gH��N�l���w_g�� � ��M��B��!J�2��f��Ut�B�5���X�J�P'���� �̚`�:AR��"V��Ra,H��s�:�c�!s�\N���w��>���YN�i>v��P���Ü5�Vz��̣�*��Q�:�M6���Q�tP�u�D�R��A
��A�F����K�bUF��J�_B)�@0����b�|Tɢ��J�Pr�eNެ	�e�;d<��dar5^�>�p�!�-����|��p!�Dr>����?M�
�      �   �   x��ν
�0��9���@�󓓟���.����R1ZP����
gz<|���O]��Ny��V�-�tS"z'��$6��������`kck�	(���u��v����%{��ܗ���G^�w})�ߤ����NwȞ������[OO      �   �  x���MO�0���_aqf����c�F�(���J�^z�����nPXP�_�1�����q�'�����ض}�A ������9s:vW�މ���v[g2�:EXg�^����Oݤ�:Y瞍?��n߶���ޘ�aw�����8����v�m{��֙7�U{i7�pյ7�|h6ݷnc��V_����z��<(��$ƨJ|�U��y���c��9	<?�!ݘcLb���n��ۻ�5戀p��`Q
qa�2��QB
0�\�=�,F,�2
�#�1�Ũ_!��x*�ӏn���5�E�����!�O�^��,�[����wHA�_&߫Ψ�b��ߎm3c�;H%��P��Vc��1M��m3��&_0Ǩ��[�YA�Al}.���	���iߵ��
���A�iq�m~w���`�x(!:���_������O���EK�祖8���h;�F���=���2��A,�d$�)�a.��@%`Ar�!px��Y��C�n��,~|��w�z��Sͻ/m�j��7��C�Cc��?"
�"kS��OZފ̅�J��P�*zM8�2O�Zڞ��^��L�: �Hy>(V�kQ���O��`�*�4�X3,�(�Y���MP�
TTHN�0���.rAvI��K��H��T��'mx��t�Z��*��,����j��/��      �   g   x�]�I
�0C�����]�8Z������:,_�H����*�m� �������/-�`ݡ�j��d�\yP���Q�/J�]�ˡ����۪�J��|$�GD��6_     