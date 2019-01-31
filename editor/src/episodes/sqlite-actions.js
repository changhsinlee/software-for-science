import React, { Component } from 'react';
import logo from '../logo.svg';
import './sqlite-actions.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch } from '@fortawesome/free-solid-svg-icons'
import classnames from 'classnames';

const Crumb = ({children}) => <div className="breadcrumb">
    {children}
</div>;
class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            hideglass: true
        }
    }
    toggle_glass = () => {
        this.setState({hideglass: !this.state.hideglass})
    }

    render() {
      return (<div className="projector" onClick={this.toggle_glass}>
            <div className="breadcrumbs">
                <Crumb className="mono">f()</Crumb>
                <Crumb>x+1</Crumb>
                <Crumb><FontAwesomeIcon icon={faSearch} /></Crumb>
            </div>
            <div className="text-editor mono">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Id consectetur purus ut faucibus pulvinar elementum integer enim. Ipsum faucibus vitae aliquet nec ullamcorper sit amet. Elit sed vulputate mi sit. Id volutpat lacus laoreet non curabitur gravida arcu ac. Bibendum ut tristique et egestas quis ipsum suspendisse ultrices gravida. Donec ultrices tincidunt arcu non sodales neque sodales ut etiam. In hendrerit gravida rutrum quisque. Eget nullam non nisi est sit amet facilisis magna. Quam elementum pulvinar etiam non. Phasellus faucibus scelerisque eleifend donec pretium. Nisl nisi scelerisque eu ultrices vitae auctor eu augue ut. Pharetra et ultrices neque ornare aenean euismod elementum. Orci eu lobortis elementum nibh tellus molestie. Eget magna fermentum iaculis eu non diam phasellus vestibulum lorem.

            Scelerisque fermentum dui faucibus in ornare quam viverra orci. Sit amet purus gravida quis blandit turpis cursus in. Platea dictumst quisque sagittis purus sit amet volutpat consequat. Pellentesque dignissim enim sit amet venenatis urna cursus eget. 
            </div>

            <div className={classnames({"blurred-box": true, "hide-glass": this.state.hideglass})}>
                This is a simple note.
            </div>
        </div>
      );
    }
  }
  
  export default App;