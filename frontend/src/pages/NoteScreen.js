import axios from "axios"
import React, { useEffect, useState } from "react"
import { useParams } from "react-router-dom"

function NoteScreen(){
    const {pk} = useParams()
    const [note, setNote] = useState(null)
    const getNote = async () => {
        try {
            const response = await axios.get(`http://localhost:8000/api/getNote/${pk}`)
            setNote(response.data)
            console.log(response)
        } catch (error) {
            
        }
    } 

    useEffect(() => {
        getNote()
    }, [])
    if(note == null)
    {
        return (    
            <p>Loading ...</p>
        )
    }
    return(
        <p>
            id = {note.id} 
            <br/>
            Name = {note.name}
            <br/>
            Description = {note.description}             
        </p>
    )
}
export default NoteScreen
