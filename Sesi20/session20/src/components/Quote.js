import React, { useEffect, useState } from 'react'

function Quote(props) {
    const [quote, setQuote] = useState(props.quote)
    useEffect(() => {
        document.title = `${quote}`
    }

    )
    return (
        <>
            <blockquote>
                {quote}
            </blockquote>
            <button onClick={() => setQuote(quote + " Haha")}>
                Click Me!
            </button>
        </>
    )
}

export default Quote