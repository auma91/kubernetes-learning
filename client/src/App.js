import React from 'react';
import List from './List'

function App() {
    return (
        <div classname="container">
            <div className="row">
				<div className="col-md-6 mx-auto">
					<h1 className="text-center">TODO</h1>
					<List/>
				</div>
			</div>
        </div>
    );
}

export default App;
