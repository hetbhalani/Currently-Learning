import express from 'express';
import { Book } from '../models/booksModel.js';

const router = express.Router();


router.post('/', async(req,res)=>{
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

router.get('/',async (req,res)=>{
    try {
        const books = await Book.find({})

        return res.status(200).json({
            count: books.length,
            data: books
        })

    } catch (error) {
        console.log(error);
        res.status(500).send({message:error.message});
    }
})

//get by id
router.get('/:id',async (req,res)=>{
    try {
        const { id } = req.params;
        const books = await Book.findById(id)

        return res.status(200).json({
            count: books.length,
            data: books
        })

    } catch (error) {
        console.log(error);
        res.status(500).send({message:error.message});
    }
})

//update book'
router.patch('/:id', async(req,res)=>{
    try {
        if(
            !req.body.title ||
            !req.body.author ||
            !req.body.publishYear
        )
        {
            return res.status(400).send({message:'Fill all the details'});
        }

        const {id} = req.params;

        const result = await Book.findByIdAndUpdate(id, req.body);
        if(!result){
            return res.status(404).json({message:"book not found"});
        }

        return res.status(200).send({message: "book updated successfully"});
    } catch (error) {
        console.log(error.message);
        res.status(500).send({message:error.message});
    }
})

//delete a book
router.delete('/:id', async(req,res)=>{
    try {
        const { id } = req.params;
        const result = await Book.findByIdAndDelete(id);

        if(!result){
            return res.status(404).json({message:"book not found"});
        }
        return res.status(200).send({message: "book deleted successfully"});

    } 
    catch (error) {
        console.log(error.message);
        res.status(500).send({message:error.message});
    }
})

export default router;  