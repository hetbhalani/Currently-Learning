import express from 'express'
import dotenv from 'dotenv';
import mongoose from 'mongoose';
import { Book } from './models/booksModel.js';
import bookRouter from './routes/bookRoutes.js'
dotenv.config();

const app = express();
const port = process.env.PORT;

app.use(express.json());

app.get('/', (req,res)=>{
    console.log(req);
    return res.status(200).send("Welcome Dostoooo!")
})


app.use('/books', bookRouter)

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