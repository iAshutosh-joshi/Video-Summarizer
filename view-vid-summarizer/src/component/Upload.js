import React from 'react';
import './upload.css';

class Upload extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: '',
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  async handleUploadImage(ev) {
    ev.preventDefault();
    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);
    data.append('filename', 'video');
    console.log("Hello");
    let response = await fetch('http://localhost:5000/upload', {
      method: 'POST',
      body: data,
    });
    console.log(response);
    let jsonData = await response.json();
    this.props.setSummary(jsonData);
  }
  render() {
    return (
      <form className='' onSubmit={this.handleUploadImage}>
        <br />
        <header className='header-class1'>OR UPLOAD FILE</header>
        <br /><br /><br />
        <span>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <button class="bn632-hover bn20">Upload</button>
        </span>
      </form>
    );
  }
}

export default Upload;