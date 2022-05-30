#!/bin/bash

: '
    This script will be used to switch git branches and pull data.
    The user will pass a branch name as parameter and also the 
    source from where the repo will be found.
'

red=`tput setaf 1`
green=`tput setaf 2`
blue=`tput setaf 4`
reset=`tput sgr0`

Help()
{
   # Display Help
   echo "${red}options:${reset}";
   echo "${red}b     To switch both free and pro to a branch. Leave empty for master.${reset}";
   echo "${red}f     To switch free to a branch.${reset}";
   echo "${red}p     To switch pro to a branch.${reset}";
   echo "${red}s     Which subdomain do you want to update? e.g. bddev/bd0/bdlive${reset}";
   echo "${red}h     Print usage information.${reset}";
   exit 1;
}

while getopts b:f:p:s:h: flag;
do
    case "${flag}" in
        h) 
            Help;
            exit 1;
            ;;
        s) subdomain=${OPTARG};;
        b) both=${OPTARG};;
        f) free=${OPTARG};;
        p) pro=${OPTARG};;
        
    esac
done

# Set pro default to master
if [[ -z "$pro" ]]
    then
        pro="master";
fi

# Set free default to master
if [[ -z "$free" ]]
    then
        free="master";
fi

# Set both default to master or init free and pro with both value
if [[ -z "$both" ]]
    then
        both="master";
    else
        free=$both;
        pro=$both;
fi

# Set subdomain default to bddev
if [[ -z "$subdomain" ]]
    then
        subdomain="bddev";
fi

# Print Status
echo "${blue}free: ${free}${reset}";
echo "${blue}pro: ${pro}${reset}";
echo "${blue}subdomain: ${subdomain}${reset}";


## Execute Tasks for FREE
echo "${green}Navigating to: ~/${subdomain}.hurayra.xyz/wp-content/plugins/betterdocs${reset}";
cd ~/${subdomain}.hurayra.xyz/wp-content/plugins/betterdocs
git fetch
git pull

echo "${green}Switching to branch: ${free}${reset}";
git checkout ${free}

echo "${green}Fetching${reset}"
git fetch
echo "${green}Pulling${reset}"
git pull

git status
git branch


## Execute Tasks for PRO
echo "${green}Navigating to: ~/${subdomain}.hurayra.xyz/wp-content/plugins/betterdocs-pro${reset}";
cd ~/${subdomain}.hurayra.xyz/wp-content/plugins/betterdocs-pro
git fetch
git pull

echo "${green}Switching to branch: ${pro}${reset}";
git checkout ${pro}

echo "${green}Fetching${reset}"
git fetch
echo "${green}Pulling${reset}"
git pull

git status
git branch


