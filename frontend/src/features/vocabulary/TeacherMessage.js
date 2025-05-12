import React from 'react';
import './TeacherMessage.css';

const TeacherMessage = () => {
  return (
    <div className="teacher-message">
      <p>Hey! That's awesome! Watching TV is a really popular thing to do.</p>

      <div className="message-section">
        <h4>[EN]</h4>
        <p>That's awesome! Watching TV is a really popular thing to do.</p>

        <div className="translation">
          <h4>[PT]</h4>
          <p>Que legal! Assistir TV é uma coisa muito popular para fazer.</p>
        </div>
      </div>

      <div className="message-section">
        <h4>[EN]</h4>
        <p>To start with, let's talk a little more about it. What <em>kind</em> of TV shows do you like? Are they comedies? Action? Something else?</p>

        <div className="translation">
          <h4>[PT]</h4>
          <p>Para começarmos, vamos conversar um pouco mais sobre isso. Que tipo de programas de TV você gosta? São comédias? Ação? Alguma outra coisa?</p>
        </div>
      </div>

      <div className="message-section">
        <h4>[Practice]</h4>
        <p>Can you tell me the name of one TV show you really enjoy? Don't worry about saying it perfectly, just try!</p>
      </div>

      <div className="message-section">
        <h4>[Pronunciation]</h4>
        <p>Let's practice saying "TV show". It's pronounced /ˈtiː.voʊ/ (tee-voe).</p>
      </div>
    </div>
  );
};

export default TeacherMessage;