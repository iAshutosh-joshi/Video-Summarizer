import Upload from "./Upload";
import YouTube from "./YoutTube";
import './Home.css';
import Summary from "../common/summary.js";
import { useState } from "react";

function Home() {
    const [summarizedText, setSummarizedText] = useState('');
    return (
        <div >
            <div style={{ display: 'flex', justifyContent: 'center' }}>
                <header className="header-class">Vid-Summarizer</header>
            </div>
            <div style={{ display: 'flex', justifyContent: 'center' }}>
                <YouTube 
                    summarizedText = {summarizedText}
                    setSummary = {setSummarizedText}
                    />
            </div>
            <hr className="hr-class"></hr>
            <div style={{ display: 'flex', justifyContent: 'center' }}>
                <Upload 
                    summarizedText = {summarizedText}
                    setSummary = {setSummarizedText}
                    />
            </div>
            <div>
                <Summary summarizedText = {summarizedText}/>
            </div>
        </div>
    );
}
export default Home;