import './summary.css';

function Summary(props) {
    return (
        <div>
            <div className='summary-header'>
                Summary
            </div>
            <div class="summary-textbox-class">
                {props.summarizedText}
            </div>
        </div>
    );
}

export default Summary;