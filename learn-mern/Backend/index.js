import express from 'express'
import dotenv from 'dotenv';
import mongoose from 'mongoose';
dotenv.config();

const app = express();
const port = process.env.PORT;

app.get('/', (req,res)=>{
    console.log(req);
    return res.status(200).send("Welcome Dostoooo!")
})

mongoose.connect(process.env.MONGO_URL)
.then(()=>{
    console.log("Connected to Database");
    app.listen(port, ()=>{
        console.log("server started!");
    })
})
.catch((err)=>{
    console.log(err);
})