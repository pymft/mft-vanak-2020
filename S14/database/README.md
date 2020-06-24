# دیتابیس 

## sqlite

* [نمونه دیتابیس](https://cdn.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip)
* [ادیتور آنلاین اس‌کیو‌ال لایت](https://sqliteonline.com/)
* [راهنمای فشرده sqlite](https://www.tutorialspoint.com/sqlite/index.htm)


## دستورهای sqlite

### ایجاد تیبل 

### اضافه کردن رکورد

### کوئری و خواندن اطلاعات 

```sql
SELECT t.name, t.milliseconds/60000, a.Title, s.Name FROM tracks  AS t 
JOIN albums AS a  ON t.trackid = a.albumid
JOIN artists as s ON a.ArtistId = s.ArtistId
WHERE s.Name = "Aerosmith"
ORDER BY t.milliseconds desc
```