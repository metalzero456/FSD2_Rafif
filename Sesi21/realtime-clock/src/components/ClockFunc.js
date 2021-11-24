import React, { useState, useEffect } from 'react'

function ClockFunctional() {
    const [time, setTime] = useState(new Date())

    const tick = () => {
        setTime(new Date())
    }

    useEffect(() => {
        const interval = setInterval(() => {tick()}, 1000)
        return function(){
            clearInterval(interval)
        }
    }, [])
    

    return (
        <div className="App-header">
            <h1>Realtime Functional Component CLOCK</h1>
            <h1>{time.toLocaleTimeString()}</h1>
        </div>
    );
}

export default ClockFunctional