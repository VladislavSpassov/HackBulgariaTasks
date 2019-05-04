select AVG(screen) from laptop

select AVG(speed) from pc  


select AVG(speed) from laptop where price > 1000 

select AVG(price) from pc where speed > 500 

select AVG(price) from pc where model in (select model from product where
        maker = "A" or type = "PC") 

select AVG(price) from (select price from pc where model in (select model
        from product where maker = "B" and type = "PC") union select price from 
       laptop where model in (select model from product where maker = "B" and ty
       pe = "Laptop")) 

select maker from product group by maker  having count(maker) >= 3 and ty
       pe = "PC"
 
select * from product where maker in (select maker from (select * from pr
       oduct where type = "PC") group by type having COUNT(maker) >= 3) and type
        = "PC"



select price,maker,product.model from pc inner join product on product.model = pc.model where pc.price = (select MAX(price) from pc)   

select AVG(cd) from pc where pc.model in (select p2.model from (select * from product as p1 where p1.type ="Printer" group by maker) p1 
inner join (select * from product as p2 where p2.type = "PC" group by maker)p2 on p1.maker = p2.maker) 
