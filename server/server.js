const express = require("express");
const app = express();

app.get("/home", (req, res) => res.send({ data: "contact" }));

app.listen(5000, () => console.log("server listening on port 5000"));
