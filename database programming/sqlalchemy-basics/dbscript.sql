-- create table: employees
CREATE TABLE employees (
    EMP_ID SMALLINT NOT NULL,
    FIRST_NAME VARCHAR (255),
    LAST_NAME VARCHAR (255),
    GENDER VARCHAR (255),
    AGE DOUBLE,
    EMAIL VARCHAR (255),
    PHONE_NR VARCHAR (255),
    EDUCATION VARCHAR (255),
    MARITAL_STAT VARCHAR (255),
    NR_OF_CHILDREN SMALLINT,
    CONSTRAINT pk_employees PRIMARY KEY (EMP_ID)
);

-- create table users 
CREATE TABLE users (
    id INTEGER NOT NULL,
    name VARCHAR,
    fullname VARCHAR,
    nickname VARCHAR,
    PRIMARY KEY (id)
);

-- create table: addresses
CREATE TABLE addresses (
    id INTEGER NOT NULL,
    email_address VARCHAR NOT NULL,
    user_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE 
                                                ON UPDATE CASCADE
);


-- insert values to table uses
delete from users;

INSERT INTO
    users (id, name, fullname, nickname)
VALUES
    (1, 'admin', 'admin', 'adm'),
    (2, 'stone', 'stone', 'S');

-- insert values to table addresses

delete from addresses;

INSERT INTO
    addresses (user_id, email_address, id)
VALUES
    (1, 'adm@smarter.com', 1),
    (2, 'stone@smarter.com', 2),
    (2, 'stone-admin@smarter.com', 3);

-- insert values to table employees

INSERT INTO
    employees (
        NR_OF_CHILDREN,
        MARITAL_STAT,
        EDUCATION,
        PHONE_NR,
        EMAIL,
        AGE,
        GENDER,
        LAST_NAME,
        FIRST_NAME,
        EMP_ID
    )
VALUES
    (
        0,
        'Single',
        'Master',
        '294-0453-82',
        's.uthaman@randatmail.com',
        27,
        'Male',
        'Uthaman',
        'Shyam',
        1001
    ),
    (
        5,
        'Single',
        'Primary',
        '485-7423-63',
        'a.hunt@randatmail.com',
        28,
        'Female',
        'Hunt',
        'Amy',
        1002
    ),
    (
        0,
        'Married',
        'Lower secondary',
        '178-1556-38',
        'm.carter@randatmail.com',
        26,
        'Female',
        'Carter',
        'Miranda',
        1003
    ),
    (
        4,
        'Married',
        'Bachelor',
        '141-6684-03',
        'm.smith@randatmail.com',
        19,
        'Male',
        'Smith',
        'Maximilian',
        1004
    ),
    (
        2,
        'Single',
        'Doctoral',
        '023-1926-55',
        'r.morgan@randatmail.com',
        20,
        'Male',
        'Morgan',
        'Rafael',
        1005
    ),
    (
        1,
        'Married',
        'Bachelor',
        '518-3606-56',
        'c.richardson@randatmail.com',
        27,
        'Male',
        'Richardson',
        'Clark',
        1006
    ),
    (
        5,
        'Single',
        'Primary',
        '453-0973-49',
        'e.parker@randatmail.com',
        29,
        'Female',
        'Parker',
        'Elise',
        1007
    ),
    (
        1,
        'Married',
        'Doctoral',
        '664-9063-19',
        'j.evans@randatmail.com',
        19,
        'Female',
        'Evans',
        'Jessica',
        1008
    ),
    (
        3,
        'Married',
        'Master',
        '010-0094-07',
        'a.west@randatmail.com',
        29,
        'Male',
        'West',
        'Adam',
        1009
    ),
    (
        3,
        'Married',
        'Upper secondary',
        '440-0085-08',
        'k.carter@randatmail.com',
        22,
        'Female',
        'Carter',
        'Kimberly',
        1010
    ),
    (
        1,
        'Married',
        'Upper secondary',
        '472-8625-83',
        'a.stewart@randatmail.com',
        30,
        'Male',
        'Stewart',
        'Alexander',
        1011
    ),
    (
        5,
        'Single',
        'Bachelor',
        '212-2154-64',
        'r.wells@randatmail.com',
        25,
        'Male',
        'Wells',
        'Robert',
        1012
    ),
    (
        3,
        'Single',
        'Doctoral',
        '696-0789-59',
        'g.owens@randatmail.com',
        26,
        'Female',
        'Owens',
        'Grace',
        1013
    ),
    (
        1,
        'Single',
        'Bachelor',
        '290-2934-09',
        'l.richards@randatmail.com',
        27,
        'Female',
        'Richards',
        'Lydia',
        1014
    ),
    (
        2,
        'Married',
        'Lower secondary',
        '671-8364-65',
        'l.andrews@randatmail.com',
        26,
        'Female',
        'Andrews',
        'Lucy',
        1015
    ),
    (
        1,
        'Married',
        'Primary',
        '658-8191-62',
        'm.ferguson@randatmail.com',
        18,
        'Male',
        'Ferguson',
        'Max',
        1016
    ),
    (
        0,
        'Single',
        'Master',
        '156-1087-43',
        't.foster@randatmail.com',
        27,
        'Female',
        'Foster',
        'Tess',
        1017
    ),
    (
        2,
        'Single',
        'Bachelor',
        '276-6868-30',
        'n.miller@randatmail.com',
        25,
        'Male',
        'Miller',
        'Ned',
        1018
    ),
    (
        3,
        'Married',
        'Upper secondary',
        '282-5750-98',
        'v.kelly@randatmail.com',
        21,
        'Female',
        'Kelly',
        'Valeria',
        1019
    ),
    (
        4,
        'Single',
        'Upper secondary',
        '110-1269-16',
        't.taylor@randatmail.com',
        19,
        'Male',
        'Taylor',
        'Tony',
        1020
    ),
    (
        4,
        'Married',
        'Lower secondary',
        '980-0639-38',
        'p.harris@randatmail.com',
        26,
        'Female',
        'Harris',
        'Paige',
        1021
    ),
    (
        5,
        'Single',
        'Primary',
        '360-8433-55',
        'h.howard@randatmail.com',
        30,
        'Female',
        'Howard',
        'Heather',
        1022
    ),
    (
        2,
        'Single',
        'Doctoral',
        '510-2471-50',
        'l.clark@randatmail.com',
        20,
        'Female',
        'Clark',
        'Lydia',
        1023
    ),
    (
        0,
        'Married',
        'Doctoral',
        '233-1267-84',
        's.myers@randatmail.com',
        27,
        'Female',
        'Myers',
        'Stella',
        1024
    ),
    (
        0,
        'Married',
        'Primary',
        '199-8052-75',
        'b.craig@randatmail.com',
        19,
        'Female',
        'Craig',
        'Belinda',
        1025
    ),
    (
        5,
        'Single',
        'Doctoral',
        '041-9655-30',
        'a.riley@randatmail.com',
        22,
        'Male',
        'Riley',
        'Abraham',
        1026
    ),
    (
        4,
        'Married',
        'Master',
        '339-7107-24',
        'e.morrison@randatmail.com',
        18,
        'Male',
        'Morrison',
        'Elian',
        1027
    ),
    (
        1,
        'Married',
        'Upper secondary',
        '780-2286-38',
        'm.stevens@randatmail.com',
        26,
        'Male',
        'Stevens',
        'Max',
        1028
    ),
    (
        1,
        'Married',
        'Master',
        '609-2425-47',
        'c.miller@randatmail.com',
        22,
        'Female',
        'Miller',
        'Cherry',
        1029
    ),
    (
        3,
        'Single',
        'Upper secondary',
        '916-3705-30',
        'g.tucker@randatmail.com',
        30,
        'Female',
        'Tucker',
        'Grace',
        1030
    ),
    (
        3,
        'Married',
        'Doctoral',
        '144-4734-39',
        'w.johnston@randatmail.com',
        22,
        'Male',
        'Johnston',
        'William',
        1031
    ),
    (
        2,
        'Single',
        'Lower secondary',
        '142-3826-97',
        'a.brown@randatmail.com',
        22,
        'Male',
        'Brown',
        'Adrian',
        1032
    ),
    (
        4,
        'Married',
        'Master',
        '966-5972-29',
        'p.brown@randatmail.com',
        30,
        'Male',
        'Brown',
        'Paul',
        1033
    ),
    (
        4,
        'Married',
        'Lower secondary',
        '887-9919-37',
        'f.cameron@randatmail.com',
        23,
        'Male',
        'Cameron',
        'Fenton',
        1034
    ),
    (
        3,
        'Single',
        'Doctoral',
        '698-2971-12',
        't.taylor@randatmail.com',
        27,
        'Male',
        'Taylor',
        'Ted',
        1035
    ),
    (
        3,
        'Single',
        'Doctoral',
        '954-1647-66',
        'd.martin@randatmail.com',
        22,
        'Male',
        'Martin',
        'Dale',
        1036
    ),
    (
        1,
        'Married',
        'Master',
        '158-0025-95',
        'r.west@randatmail.com',
        18,
        'Male',
        'West',
        'Reid',
        1037
    ),
    (
        2,
        'Married',
        'Upper secondary',
        '439-0151-08',
        'e.adams@randatmail.com',
        27,
        'Female',
        'Adams',
        'Eleanor',
        1038
    ),
    (
        0,
        'Married',
        'Master',
        '369-1431-89',
        'n.clark@randatmail.com',
        19,
        'Male',
        'Clark',
        'Nicholas',
        1039
    ),
    (
        5,
        'Married',
        'Primary',
        '210-5428-23',
        'j.brown@randatmail.com',
        29,
        'Female',
        'Brown',
        'Jasmine',
        1040
    ),
    (
        1,
        'Married',
        'Primary',
        '255-5384-28',
        'e.perkins@randatmail.com',
        21,
        'Female',
        'Perkins',
        'Eleanor',
        1041
    ),
    (
        1,
        'Married',
        'Master',
        '140-4867-24',
        's.johnston@randatmail.com',
        25,
        'Male',
        'Johnston',
        'Sawyer',
        1042
    ),
    (
        5,
        'Single',
        'Bachelor',
        '508-7881-03',
        'a.nelson@randatmail.com',
        29,
        'Male',
        'Nelson',
        'Abraham',
        1043
    ),
    (
        0,
        'Married',
        'Master',
        '371-9535-85',
        'd.elliott@randatmail.com',
        30,
        'Male',
        'Elliott',
        'Derek',
        1044
    ),
    (
        1,
        'Single',
        'Primary',
        '204-9991-01',
        'm.ferguson@randatmail.com',
        27,
        'Female',
        'Ferguson',
        'Miley',
        1045
    ),
    (
        3,
        'Married',
        'Lower secondary',
        '078-5303-41',
        't.watson@randatmail.com',
        29,
        'Male',
        'Watson',
        'Tyler',
        1046
    ),
    (
        4,
        'Single',
        'Upper secondary',
        '518-9796-70',
        'a.perry@randatmail.com',
        28,
        'Female',
        'Perry',
        'Amanda',
        1047
    ),
    (
        4,
        'Single',
        'Doctoral',
        '699-6809-85',
        'c.higgins@randatmail.com',
        29,
        'Female',
        'Higgins',
        'Cherry',
        1048
    ),
    (
        2,
        'Single',
        'Lower secondary',
        '130-8103-40',
        'd.allen@randatmail.com',
        26,
        'Female',
        'Allen',
        'Deanna',
        1049
    ),
    (
        0,
        'Single',
        'Bachelor',
        '347-7059-66',
        'v.ellis@randatmail.com',
        28,
        'Female',
        'Ellis',
        'Vanessa',
        1050
    ),
    (
        2,
        'Married',
        'Batchler',
        '138xxx',
        'stone@126.com',
        20,
        'Male',
        'Wang',
        'Stone',
        9001
    );


