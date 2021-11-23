import React, { Component, useEffect, useState } from 'react'
import Quote from './Quote'

function PersonInformation() {
    const [name, setName] = useState("Rafif")
    const [nameField, setNameField] = useState("")
    const [age, setAge] = useState(22)
    const [quote, setQuote] = useState("Tiada hari tanpa ngoding")

    const changeName = () => {
        setName("Taqiuddin")
    }

    const inputsHandler = (e) => {
        setNameField( {[e.target.name]: e.target.value})
    }

    const addAge = () => {
        setAge(age + 1)
    }

    const decreaseAge = () => {
        setAge(age - 1)
    }

    return (
        <>
            <h1>Person Information</h1>
            
            <div>
                <span>Name: {name}</span><br />
                <span>Age: {age}</span><br />
                <button onClick={addAge}>Add Age</button>
                <button onClick={decreaseAge}>Decrease Age</button>
                {/* <input type="text" name="name" value={nameField}/> */}
                <button onClick={changeName}>Change Name!</button>
                <Quote quote={quote} />
            </div>
        </>
    )
}

// class PersonInformation extends Component {
//     constructor () {
//         super()

//         this.state = {
//             name: "Rafif",
//             age: 22,
//             quote: "Tiada hari tanpa ngoding React"
//         }
//     }

//     render() {
//         return (
//             <>
//                 <h1>Person Information</h1>
//                 <div>
//                     <span>Name: {this.state.name}</span><br/>
//                     <span>Age: {this.state.age}</span><br/>
//                     <Quote quote={this.state.quote}/>
//                 </div>
//             </>
//         )
//     }
// }

export default PersonInformation