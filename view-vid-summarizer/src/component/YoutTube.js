import { useState } from 'react';
import './youtube.css';
function YouTube(props) {
    const [youtubeUrl, setYoutubeUrl] = useState('');
    const handleClick = async(yurl) =>{
        console.log(yurl);
        let response = await fetch('http://localhost:5000/link?' + new URLSearchParams({
            youtubeUrl: yurl
        }));
        console.log(response);
        const jsonData = await response.json();
        props.setSummary(jsonData);
    }
    return (
        <div>
            <br /><br /><br /><br />
            <span>
                <input type="text" id="youtube-url" placeholder="YouTube Url..." value={youtubeUrl} onChange={e => setYoutubeUrl(e.target.value)}/>
                <button class="bn632-hover bn20" onClick={() => handleClick(youtubeUrl)}>Summarize</button>
            </span>
        </div>
    );
}
export default YouTube;