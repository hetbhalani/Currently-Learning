import express from 'express'
import dotenv from 'dotenv';
import mongoose from 'mongoose';
import { Book } from './models/booksModel.js';
dotenv.config();

const app = express();
const port = process.env.PORT;

app.use(express.json());

app.get('/', (req,res)=>{
    console.log(req);
    return res.status(200).send("Welcome Dostoooo!")
})


app.post('/books', async(req,res)=>{
    try {
        if(
            !req.body.title ||
            !req.body.author ||
            !req.body.publishYear
        )
        {
            return res.status(400).send({message:'Fill all the details'});
        }

        const newBook = {
           title:  req.body.title, 
           author: req.body.author,
           publishYear: req.body.publishYear
        }

        const book = await Book.create(newBook);

        return res.status(201).send(book)
    } catch (error) {
        console.log(error);
        res.status(500).send({message:error.message});
    }
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