<?php

use XF\AddOn\AbstractSetup;

class Setup extends AbstractSetup
{
	public function install(array $stepParams = []) {
		include dirname(__FILE__) . "/_data/Options.php";
		copy(dirname(__FILE__) . "/_data/Entity.php", $_SERVER['DOCUMENT_ROOT'] . $newpath);
	}

	public function upgrade(array $stepParams = []) {
		include dirname(__FILE__) . "/_data/Options.php";
		copy(dirname(__FILE__) . "/_data/Entity.php", $_SERVER['DOCUMENT_ROOT'] . $newpath);
	}

	public function uninstall(array $stepParams = []) {
		include dirname(__FILE__) . "/_data/Options.php";
		$newfile = $_SERVER['DOCUMENT_ROOT'] . $newpath;

		if (!file_exists($newfile)) {
			copy(dirname(__FILE__) . "/_data/Entity.php", $newfile);
		}
	}
}
