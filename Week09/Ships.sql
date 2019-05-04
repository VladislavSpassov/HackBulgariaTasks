select name,country, numguns ,launched from `CLASSES` inner join `SHIPS` on `CLASSES`.`CLASS` = `SHIPS`.`CLASS`      

select ship from `OUTCOMES` where battle in ( select name from `BATTLES` where `DATE` like "%1942%")

select * from `SHIPS` where `NAME` not in (select ship from `OUTCOMES`)  

 select name,country, numguns ,launched from `CLASSES` inner join `SHIPS` on `CLASSES`.`CLASS` = `SHIPS`.`CLASS` union select name,country, numguns,launched from
           `CLASSES` inner join `SHIPS` on `CLASSES`.`CLASS` = `SHIPS`.`NAME`      



