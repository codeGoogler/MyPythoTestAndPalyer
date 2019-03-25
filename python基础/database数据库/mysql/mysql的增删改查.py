#
# //常见一个表
# CREATE TABLE students (
#     id int(11)  AUTO_INCREMENT NOT NULL ,
#     name varchar(10) NOT NULL,
#     birthday DATE  DEFAULT NULL,
#     sex char NOT NULL,
#     gender bit DEFAULT 1,
#     isDelete bit DEFAULT 0,
#     PRIMARY KEY (id)
# )
#
#
# INSERT INTO students (name,birthday,sex,gender,isDelete) VALUES("张三","2018-5-21 14:34:23","男",1,0)
#
# INSERT INTO students (name,birthday,sex,gender,isDelete) VALUES("翠花",NULL,"女",1,0)
#
# INSERT INTO students (name,sex) VALUES("卡卡罗特","男")
#
# //查询所有的内容
# SELECT * from students WHERE sex = "男"
#
# // 修改表
# UPDATE students SET birthday = "1990-04-11" WHERE birthday IS NULL
#
#
#
# //增加一列
# ALTER TABLE students add age int(11) DEFAULT 0
#
#
#
# //根据条件进行删除
# DELETE   FROM students WHERE age > 22