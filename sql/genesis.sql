DROP DATABASE kBlog;
CREATE DATABASE kBlog;
USE kBlog;

CREATE TABLE posts(
	id INT AUTO_INCREMENT,
	title TEXT,
	content TEXT,
	author TEXT,
	publish BOOLean NOT NULL DEFAULT false,
	date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,	
	primary key (id)
);

INSERT INTO posts VALUES(
	NULL,
	'Post one',
	'Burger patties 
	are awesome!',
	'Kiddi',
	1,
	NOW()
);

INSERT INTO posts VALUES(
	NULL,
	'Post two',
	'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer eget tellus gravida, porta dui nec, tristique sem. Ut malesuada dui ac mattis porta. Curabitur vehicula volutpat neque, non adipiscing magna ultrices vel. Fusce pretium in enim et ultrices. Praesent lacinia auctor metus. Phasellus adipiscing odio id elit ultricies lacinia. Donec venenatis diam in justo commodo, non tempor est porttitor. Curabitur nec velit ac diam posuere rhoncus. Suspendisse scelerisque mi id facilisis faucibus. Proin eu feugiat odio. Praesent luctus, libero ut venenatis facilisis, sapien lacus rhoncus ipsum, eget vehicula lacus elit at lorem. Phasellus sollicitudin enim urna, eu auctor augue gravida a. Mauris semper, dolor eget pellentesque fermentum, tellus sem bibendum neque, at feugiat mauris tellus ut est. Quisque tincidunt dolor non magna pretium vestibulum. Duis sit amet ipsum malesuada, fermentum ipsum sed, imperdiet lorem. Mauris scelerisque sem ut diam ultrices elementum.

Phasellus erat turpis, consequat vel mi ac, bibendum consequat augue. Vestibulum mi ipsum, varius sit amet lorem ut, dapibus tincidunt nulla. Maecenas fermentum, eros sed facilisis porttitor, lorem lacus sodales mi, nec volutpat magna erat id lorem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id pretium purus. Aliquam erat volutpat. In consequat eu metus ut ultricies. Etiam et risus dignissim, cursus massa eget, auctor est. Mauris dapibus justo nibh, scelerisque interdum lacus ultricies non. Ut varius lorem et dui dignissim, sed adipiscing odio tincidunt. Praesent sagittis pulvinar tortor eget varius. Duis tempor ligula urna, ac sodales ligula ornare nec. Quisque malesuada nec turpis sit amet rutrum.

Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Phasellus eu ipsum porttitor nisl eleifend pellentesque vel at justo. Praesent tincidunt hendrerit ante sed scelerisque. Nam dictum nulla non magna porttitor, nec ullamcorper sem aliquet. Donec dictum venenatis rutrum. Curabitur ut lorem sed turpis ultrices sollicitudin pretium rhoncus ipsum. Maecenas eu lectus leo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam nec orci lorem.

Donec cursus turpis id orci placerat porta. Integer aliquam pretium luctus. Nullam non mauris nec tellus sagittis placerat vel a mi. Aliquam erat volutpat. Nulla adipiscing vehicula adipiscing. Donec commodo elementum felis malesuada imperdiet. Duis neque metus, rhoncus sit amet augue quis, dignissim iaculis elit. Nam at elit nec magna consequat egestas. Etiam quis tellus tincidunt orci dignissim dictum. Vivamus ac placerat massa. Vestibulum id tincidunt nisi, id iaculis dolor.

Sed tincidunt interdum lacus sed luctus. Etiam velit erat, sagittis sed neque vitae, tristique tempus felis. Suspendisse semper ipsum id purus lacinia, vitae condimentum sem aliquet. Nunc accumsan bibendum commodo. Duis quis ligula nisi. In sollicitudin metus vel pulvinar aliquam. Fusce rutrum faucibus magna, quis porta elit iaculis in. Duis ante quam, volutpat ut dapibus eu, consectetur vitae tellus. Nam eu molestie ante. Quisque vel massa id lacus euismod volutpat.',
	'Kiddi',
	1,
	NOW()
);