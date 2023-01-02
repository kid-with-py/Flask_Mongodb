var db = connect("mongodb://admin:root@localhost:27017/admin");
db = db.getSiblingDB('admin');
db.createUser(
    {
        user: "admin",
        pwd: "root",
        roles: [
            {
                role: "readWrite",
                db: "admin"
            }
        ]
    }
);
