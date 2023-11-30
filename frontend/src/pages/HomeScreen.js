import React, { useEffect, useState } from "react";
import { Col, Container, Row } from "react-bootstrap";
import { ReactComponent as Hashtag } from "../assets/hashtag.svg";
import axios from "axios"
import { Link, useNavigate } from "react-router-dom";

function HomeScreen() {

    const[notes, setNotes] = useState([]) 
    const navigate = useNavigate()

    async function getNotes()
    {
        try
        {
            const response = await axios.get("http://localhost:8000/api/getNotes/all")
            console.log(response.data)
            setNotes(response.data.data)
        }
        catch(e)
        {
            console.log(e)
        }
    }

   const handleNavigate = (id) => {
    navigate(`/noteScreen/${id}`)
   }


    useEffect(() =>{
        getNotes()
    }, [])
    
    return (
        <div style={{ background: "black", width: "100vw", height: "100vh", position: "relative", display: "flex", alignItems: "center", justifyContent: "center" }}>
            <Container style={{ background: "white", width: "30%", height: "80%" }}>
                <Row style={{ borderBottom: "1px solid #e6e6e6", padding: "5px" }}>
                    <strong>
                        My Notes
                    </strong>
                </Row>

                <Row>
                    <Col md={2} >
                        <Hashtag />
                    </Col>
                    <Col md={2}>
                        Notes
                    </Col>
                    <Col md={6} style={{ display: "flex", alignItems: "end", justifyContent: "flex-end" }}>
                        0
                    </Col>
                </Row>
                <div>
                    {
                        notes.map(note => <Row style={{border: "1px solid black", marginTop: "3px", cursor: "pointer"}}>
                            <Container style={{textDecoration: "none"}} onClick={ () => handleNavigate(note.id) } >{note.name}</Container>
                        </Row>)
                    }
                </div>
            </Container>
        </div>
    )
}
export default HomeScreen   