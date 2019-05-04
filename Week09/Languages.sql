create table languages(ID int not null primary key, language varchar(
           200),answer varchar(200), answered bool, guide varchar(200)); 


insert into  languages values(1,"Python","google",0, "A folder named Python was created. Go there and fight with program.py!"); 

insert into  languages values(2,"Go","200 OK",0, "A folder named Go was created. Go there and try to make Google Go run."); 


insert into  languages values(3,"Java","object oriented programming",0, "A folder named Java was created. Can you handle the class?"); 

insert into  languages values(4,"Haskell","Lambda",0, "Something pure has landed. Go to Haskell folder and see it!"); 

insert into  languages values(5,"C#","NDI=",0, "Do you see sharp? Go to the C# folder and check out."); 

insert into  languages values(6,"Ruby","https://www.ruby-lang.org/bg/",0,"Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!"); 

insert into  languages values(7,"C++","header files",0, "Here be dragons! It is C++ time. Go to the C++ folder."); 

insert into  languages values(8,"JavaScript","Douglas Crockford",0,"NodeJS time. Go to JavaScript folder and Node your way!"); 


alter table languages add rating int ;

create table new_languages(ID int not null primary key, language varchar( 
                      200),answer varchar(200), answered bool, guide varchar(200),rating int, CHECK(rating >= 1 and rating <= 9));

insert into new_languages select * from languages; 
 

DROP TABLE languages;

ALTER TABLE new_languages RENAME TO languages;


UPDATE languages set answered = 1 where language = "Go" or language = "Python"; 

select language from languages where answer = "200 OK" or answer = "Lambda"; 

