from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import the flask app
# app = Flask(__name__)

# define the database connection string for Flask app
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# TODO: Create db from Flask app
db = SQLAlchemy(app)

# some tool source, tool_version, data_source have length constraints
# need to add default of current timestamp for data_collection_date


class AnalysisLog(db.Model):
    __tablename__ = 'analysis_log'
    repos_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(), nullable=False)
    date_attempted = db.Column(db.TIMESTAMP(), nullable=False)


class ChaossMetricStatus(db.Model):
    __tablename__ = 'chaoss_metric_status'
    cms_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    cm_group = db.Column(db.BigInteger)
    cm_source = db.Column(db.String()
    cm_type = db.Column(db.String())
    cm_backend_status = db.Column(db.String())
    cm_frontend_status = db.Column(db.String())
    cm_defined = db.Column(db.Boolean())
    cm_api_endpoint_repo = db.Column(db.String())
    cm_api_endpoint_rg = db.Column(db.String())
    cm_name = db.Column(db.String())
    cm_working_group = db.Column(db.String())
    cm_info = db.Column(db.JSON())
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())
    cm_working_group_focus_area = db.Column(db.String())




class CommitCommentRef(db.Model):
    __tablename__ = 'commit_comment_ref'
    cmt_comment_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    cmt_id = db.Column(db.BigInteger, nullable=False)
    repo_id = db.Column(db.BigInteger)
    msg_id = db.Column(db.BigInteger, nullable=False)
    user_id = db.Column(db.BigInteger, nullable=False)
    body = db.Column(db.Text())
    line = db.Column(db.BigInteger)
    position = db.Column(db.BigInteger)
    commit_comment_src_node_id = db.Column(db.String())
    cmt_comment_src_id = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.TIMESTAMP(), nullable=False)
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())


class Commits(db.Model):
    __tablename__ = 'commits'
    cmt_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    repo_id = db.Column(db.BigInteger, nullable=False)
    cmt_commit_hash = db.Column(db.String(80), nullable=False)
    cmt_author_name = db.Column(db.String(), nullable=False)
    cmt_author_raw_email = db.Column(db.String(), nullable=False)
    cmt_author_email = db.Column(db.String(), nullable=False)
    cmt_author_date = db.Column(db.VARCHAR(length=10), nullable=False)
    cmt_author_affiliation = db.Column(db.String())
    cmt_committer_name = db.Column(db.String(), nullable=False)
    cmt_committer_raw_email = db.Column(db.String(), nullable=False)
    cmt_committer_email = db.Column(db.String(), nullable=False)
    cmt_committer_date = db.Column(db.String(), nullable=False)
    cmt_committer_affiliation = db.Column(db.String())
    cmt_added = db.Column(db.Integer, nullable=False)
    cmt_removed = db.Column(db.Integer, nullable=False)
    cmt_whitespace = db.Column(db.Integer, nullable=False)
    cmt_filename = db.Column(db.String(), nullable=False)
    cmt_date_attempted = db.Column(db.TIMESTAMP(), nullable=False)
    cmt_ght_author_id = db.Column(db.Integer)
    cmt_ght_committer_id = db.Column(db.Integer)
    cmt_ght_committed_at = db.Column(db.TIMESTAMP())
    cmt_committer_timestamp = db.Column(db.TIMESTAMP())
    cmt_author_timestamp = db.Column(db.TIMESTAMP())
    cmt_author_platform_username = db.Column(db.String())
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

class ContributorAffiliations(db.Model):
    __tablename__ = 'contributor_affiliations'
    ca_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    ca_domain = db.Column(db.String(length=64), nullable=False)
    ca_start_date = db.Column(db.Date)
    tool_source = db.Column(db.String(length=255))
    tool_version = db.Column(db.String(length=255))
    data_source = db.Column(db.String(length=255))
    data_collection_date = db.Column(db.TIMESTAMP())
    ca_last_used = db.Column(db.TIMESTAMP(), nullable=False)
    ca_affiliation = db.Column(db.String())
    ca_active = db.Column(db.SmallInteger)

class ContributorRepo(db.Model):
    __tablename__ = 'contributor_repo'
    cntrb_repo_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    cntrb_id = db.Column(db.BigInteger, nullable=False)
    repo_git = db.Column(db.String(), nullable=False)
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())
    repo_name = db.Column(db.String(length=255), nullable=False)
    gh_repo_id = db.Column(db.BigInteger, nullable=False)
    cntrb_category = db.Column(db.String(length=255))
    event_id = db.Column(db.BigInteger)
    created_at = db.Column(db.TIMESTAMP())

class Contributors(db.Model):
    __tablename__ = 'contributors'
    cntrb_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    cntrb_login = db.Column(db.String())
    cntrb_email = db.Column(db.String())
    cntrb_full_name = db.Column(db.String())
    cntrb_company = db.Column(db.String())
    cntrb_created_at = db.Column(db.TIMESTAMP())
    cntrb_type = db.Column(db.String())
    cntrb_fake = db.Column(db.SmallInteger)
    cntrb_deleted = db.Column(db.SmallInteger)
    cntrb_long = db.Column(db.Numeric(precision=11, scale=8))
    cntrb_lat = db.Column(db.Numeric(precision=10, scale=8))
    cntrb_country_code = db.Column(db.CHAR(length=3))
    cntrb_state = db.Column(db.String())
    cntrb_city = db.Column(db.String())
    cntrb_location = db.Column(db.String())
    cntrb_canonical = db.Column(db.String())
    cntrb_last_used = db.Column(db.TIMESTAMP())
    gh_user_id = db.Column(db.BigInteger)
    gh_login = db.Column(db.String())
    gh_url = db.Column(db.String())
    gh_html_url = db.Column(db.String())
    gh_node_id = db.Column()db.String())
    gh_avatar_url = db.Column(db.String())
    gh_gravatar_id = db.Column(db.String())
    gh_followers_url = db.Column(db.String())
    gh_following_url = db.Column(db.String())
    gh_gists_url = db.Column(db.String())
    gh_starred_url = db.Column(db.String())
    gh_subscriptions_url = db.Column(db.String())
    gh_organizations_url = db.Column(db.String())
    gh_repos_url = db.Column(db.String())
    gh_events_url = db.Column(db.String())
    gh_received_events_url = db.Column(db.String())
    gh_type = db.Column(db.String())
    gh_site_admin = db.Column(db.String())
    gl_web_url = db.Column(db.String())
    gl_avatar_url = db.Column(db.String())
    gl_state = db.Column(db.String())
    gl_username = db.Column(db.String())
    gl_full_name = db.Column(db.String())
    gl_id = db.Column(db.BigInteger)
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

class ContributorAliases(db.Model):
    __tablename__ = 'contributor_aliases'
    cntrb_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    cntrb_a_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    canonical_email = db.Column(db.String(), nullable=False)
    alias_email = db.Column(db.String(length=128), nullable=False)
    cntrb_active = db.Column(db.SmallInteger, nullable=False)
    cntrb_last_modified = db.Column(db.TIMESTAMP(), nullable=False)
    tool_source = db.Column(db.String(length=255))
    tool_version = db.Column(db.String(length=255))
    data_source = db.Column(db.String(length=255))
    data_collection_date = db.Column(db.TIMESTAMP())

class IssueAssignees(db.Model):
    __tablename__ = 'issue_assignees'
    issue_assignee_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    issue_id = db.Column(db.BigInteger)
    cntrb_id = db.Column(db.BigInteger)
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

class IssueEvents(db.Model):
    __tablename__ = 'issue_events'
    event_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    issue_id = db.Column(db.BigInteger, nullable=False)
    cntrb_id = db.Column(db.BigInteger, nullable=False)
    action = db.Column(db.String(255), nullable=False)
    action_commit_hash = db.Column(db.String())
    created_at = db.Column(db.TIMESTAMP(), nullable=False)
    node_id = db.Column(db.String())
    node_url = db.Column(db.String())
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

class IssueLabels(db.Model):
    __tablename__ = 'issue_labels'
    issue_label_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    issue_id = db.Column(db.BigInteger)
    label_text = db.Column(db.String())
    label_description = db.Column(db.String())
    label_color = db.Column(db.String())
    tool_source = db.Column(db.String(255))
    tool_version = db.Column(db.String(255))
    data_source = db.Column(db.String(255))
    data_collection_date = db.Column(db.TIMESTAMP())
    label_src_id = db.Column(db.BigInteger)
    label_src_node_id = db.Column(db.String())

class IssueMessageRef(db.Model):
    __tablename__ = 'issue_message_ref'
    issue_msg_ref_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    issue_id = db.Column(db.BigInteger)
    repo_id = db.Column(db.BigInteger)
    msg_id = db.Column(db.BigInteger)
    issue_msg_ref_src_node_id = db.Column(db.String())
    issue_msg_ref_src_comment_id = db.Column(db.BigInteger)
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

# should repo_id be allowed to be NULL?

class Issues(db.Model):
    __tablename__ = 'issues'
    issue_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    repo_id = db.Column(db.BigInteger)
    reporter_id = db.Column(db.BigInteger)
    pull_request = db.Column(db.BigInteger)
    pull_request_id = db.Column(db.BigInteger)
    created_at = db.Column(db.TIMESTAMP())
    issue_title = db.Column(db.String())
    issue_body = db.Column(db.String())
    cntrb_id = db.Column(db.BigInteger)
    comment_count = db.Column(db.BigInteger)
    updated_at = db.Column(db.TIMESTAMP())
    closed_at = db.Column(db.TIMESTAMP())
    due_on = db.Column(db.TIMESTAMP())
    repository_url = db.Column(db.String())
    issue_url = db.Column(db.String())
    labels_url = db.Column(db.String())
    comments_url = db.Column(db.String())
    events_url = db.Column(db.String())
    html_url = db.Column(db.String())
    issue_state = db.Column(db.String())
    issue_node_id = db.Column(db.String())
    gh_issue_number = db.Column(db.BigInteger)
    gh_issue_id = db.Column(db.BigInteger)
    gh_user_id = db.Column(db.BigInteger)
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

class Message(db.Model):
    __tablename__ = 'message'
    msg_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    rgls_id = db.Column(db.BigInteger)
    platform_msg_id = db.Column(db.BigInteger)
    platform_node_id = db.Column(db.String())
    repo_id = db.Column(db.BigInteger)
    cntrb_id = db.Column(db.BigInteger)
    msg_text = db.Column(db.String())
    msg_timestamp = db.Column(db.TIMESTAMP())
    msg_sender_email = db.Column(db.String())
    msg_header = db.Column(db.String())
    pltfrm_id = db.Column(db.BigInteger, nullable=False)
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

class MessageAnalysis(db.Model):
    __tablename__ = 'message_analysis'
    msg_analysis_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    msg_id = db.Column(db.BigInteger)
    worker_run_id = db.Column(db.BigInteger)
    sentiment_score = db.Column(db.Float())
    reconstruction_error = db.Column(db.Float())
    novelty_flag = db.Column(db.Boolean())
    feedback_flag = db.Column(db.Boolean())
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

class MessageAnalysisSummary(db.Model):
    __tablename__ = 'message_analysis_summary'
    msg_summary_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    repo_id = db.Column(db.BigInteger)
    worker_run_id = db.Column(db.BigInteger)
    positive_ratio = db.Column(db.Float())
    negative_ratio = db.Column(db.Float())
    novel_count = db.Column(db.BigInteger)
    period = db.Column(db.TIMESTAMP())
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

class Platform(db.Model):
    __tablename__ = 'platform'
    pltfrm_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    pltfrm_name = db.Column(db.String(length=255))
    pltfrm_version = db.Column(db.String(length=255))
    pltfrm_release_date = db.Column(db.Date)
    tool_source = db.Column(db.String(length=255))
    tool_version = db.Column(db.String(length=255))
    data_source = db.Column(db.String(length=255))
    data_collection_date = db.Column(db.TIMESTAMP())

class PullRequestMessageRef(db.Model):
    __tablename__ = 'pull_request_message_ref'
    pr_msg_ref_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    pull_request_id = db.Column(db.BigInteger)
    repo_id = db.Column(db.BigInteger)
    msg_id = db.Column(db.BigInteger)
    pr_message_ref_src_comment_id = db.Column(db.String())
    pr_message_ref_src_node_id = db.Column(db.BigInteger)
    pr_issue_url = db.Column(db.String())
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

class PullRequestReviewMessageRef(db.Model):
    __tablename__ = 'pull_request_review_message_ref'
    pr_review_msg_ref_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    pr_review_id = db.Column(db.BigInteger)
    repo_id = db.Column(db.BigInteger)
    msg_id = db.Column(db.BigInteger)
    pr_review_msg_url = db.Column(db.String())
    pr_review_src_id = db.Column(db.BigInteger)
    pr_review_msg_src_id = db.Column(db.BigInteger)
    pr_review_msg_node_id = db.Column(db.String())
    pr_review_msg_diff_hunk = db.Column(db.String())
    pr_review_msg_path = db.Column(db.String())
    pr_review_msg_position = db.Column(db.BigInteger)
    pr_review_msg_original_position = db.Column(db.BigInteger)
    pr_review_msg_commit_id = db.Column(db.String())
    pr_review_msg_original_commit_id = db.Column(db.String())
    pr_review_msg_updated_at = db.Column(db.TIMESTAMP())
    pr_review_msg_html_url = db.Column(db.String())
    pr_url = db.Column(db.String())
    pr_review_msg_author_association = db.Column(db.String())
    pr_review_msg_start_line = db.Column(db.BigInteger)
    pr_review_msg_original_start_line = db.Column(db.BigInteger)
    pr_review_msg_start_side = db.Column(db.String())
    pr_review_msg_line = db.Column(db.BigInteger)
    pr_review_msg_original_line = db.Column(db.BigInteger)
    pr_review_msg_side = db.Column(db.String())
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

class Pull_Requests(db.Model):
    __tablename__ = 'pull_requests'
    pull_request_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    repo_id = db.Column(db.BigInteger)
    pr_url = db.Column(db.String())
    pr_src_id = db.Column(db.BigInteger)
    pr_src_node_id = db.Column(db.String())
    pr_html_url = db.Column(db.String())
    pr_diff_url = db.Column(db.String())
    pr_patch_url = db.Column(db.String())
    pr_issue_url = db.Column(db.String())
    pr_augur_issue_id = db.Column(db.BigInteger)
    pr_src_number = db.Column(db.BigInteger)
    pr_src_state = db.Column(db.String())
    pr_src_locked = db.Column(db.Boolean())
    pr_src_title = db.Column(db.String())
    pr_augur_contributor_id = db.Column(db.BigInteger)
    pr_body = db.Column(db.Text())
    pr_created_at = db.Column(db.TIMESTAMP())
    pr_updated_at = db.Column(db.TIMESTAMP())
    pr_closed_at = db.Column(db.TIMESTAMP())
    pr_merged_at = db.Column(db.TIMESTAMP())
    pr_merge_commit_sha = db.Column(db.String())
    pr_teams = db.Column(db.BigInteger)
    pr_milestone = db.Column(db.String())
    pr_commits_url = db.Column(db.String())
    pr_review_comments_url = db.Column(db.String())
    pr_review_comment_url = db.Column(db.String())
    pr_comments_url = db.Column(db.String())
    pr_statuses_url = db.Column(db.String())
    pr_meta_head_id = db.Column(db.String())
    pr_meta_base_id = db.Column(db.String())
    pr_src_issue_url = db.Column(db.String())
    pr_src_comments_url = db.Column(db.String())
    pr_src_review_comments_url = db.Column(db.String())
    pr_src_commits_url = db.Column(db.String())
    pr_src_statuses_url = db.Column(db.String())
    pr_src_author_association = db.Column(db.String())
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

class PullRequestCommits(db.Model):
    __tablename__ = 'pull_request_commits'
    pr_cmt_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    pull_request_id = db.Column(db.BigInteger)
    pr_cmt_sha = db.Column(db.String())
    pr_cmt_node_id = db.Column(db.String())
    pr_cmt_message = db.Column(db.String())
    #TODO: varbit in database can't find sqlalchemy equivalent
    pr_cmt_comments_url = db.Column(db.String())
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())
    pr_cmt_author_cntrb_id = db.Column(db.BigInteger)
    pr_cmt_timestamp = db.Column(db.TIMESTAMP())
    pr_cmt_author_email = db.Column(db.String())

class PullRequestEvents(db.Model):
    __tablename__ = 'pull_request_events'
    pr_event_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    pull_request_id = db.Column(db.BigInteger, nullable=False)
    cntrb_id = db.Column(db.BigInteger, nullable=False)
    action = db.Column(db.String(length=255), nullable=False)
    action_commit_hash = db.Column(db.String())
    created_at = db.Column(db.TIMESTAMP(), nullable=False)
    issue_event_src_id = db.Column(db.BigInteger)
    node_id = db.Column(db.String())
    node_url = db.Column(db.String())
    tool_source = db.Column(db.String(length=255))
    tool_version = db.Column(db.String(length=255))
    data_source = db.Column(db.String(length=255))
    data_collection_date = db.Column(db.TIMESTAMP())

class PullRequestFiles(db.Model):
    __tablename__ = 'pull_request_files'
    pull_request_id = db.Column(db.BigInteger)
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())
    pr_file_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    pr_file_additions = db.Column(db.BigInteger)
    pr_file_deletions = db.Column(db.BigInteger)
    pr_file_path = db.Column(db.String())

class PullRequestLabels(db.Model):
    __tablename__ = 'pull_request_labels'
    pr_label_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    pull_request_id = db.Column(db.BigInteger)
    pr_src_id = db.Column(db.BigInteger)
    pr_src_node_id = db.Column(db.String())
    pr_src_url = db.Column(db.String())
    pr_src_description = db.Column(db.String())
    pr_src_color = db.Column(db.String())
    pr_src_default_bool = db.Column(db.Boolean())
    tool_source = db.Column(db.String(length=255))
    tool_version = db.Column(db.String(length=255))
    data_source = db.Column(db.String(length=255))
    data_collection_date = db.Column(db.TIMESTAMP())

class Repo(db.Model):
    __tablename__ = 'repo'
    repo_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    repo_group_id = db.Column(db.BigInteger, nullable=False)
    repo_git = db.Column(db.String(), nullable=False)
    repo_path = db.Column(db.String())
    repo_name = db.Column(db.String())
    repo_added = db.Column(db.TIMESTAMP(), nullable=False)
    repo_status = db.Column(db.String(), nullable=False)
    repo_type = db.Column(db.String())
    url = db.Column(db.String())
    owner_id = db.Column(db.Integer)
    description = db.Column(db.String())
    primary_language = db.Column(db.String())
    created_at = db.Column(db.String())
    forked_from = db.Column(db.String())
    updated_at = db.Column(db.TIMESTAMP())
    repo_archived_date_collected = db.Column(db.TIMESTAMP())
    repo_archived = db.Column(db.Integer)
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())

class RepoGroups(db.Model):
    __tablename__ = 'repo_groups'
    repo_group_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    rg_name = db.Column(db.String(), nullable=False)
    rg_description = db.Column(db.String())
    rg_website = db.Column(db.String(length=128))
    rg_recache = db.Column(db.SmallInteger)
    rg_last_modified = db.Column(db.TIMESTAMP(), nullable=False)
    rg_type = db.Column(db.String())
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())


    # Template for model class
    """
    class Pull_Requests(db.Model):
    __tablename__ = 'pull_requests'
    pull_request_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    repo_id = db.Column(db.BigInteger)
    pr_url = db.Column()
    pr_src_id = db.Column()
    pr_src_node_id = db.Column()
    pr_html_url = db.Column()
    pr_diff_url = db.Column()
    pr_patch_url = db.Column()
    pr_issue_url = db.Column()
    pr_augur_issue_id = db.Column()
    pr_src_number = db.Column()
    pr_src_state = db.Column()
    pr_src_locked = db.Column()
    pr_src_title = db.Column()
    pr_augur_contributor_id = db.Column()
    pr_body = db.Column()
    pr_created_at = db.Column()
    pr_updated_at = db.Column()
    pr_closed_at = db.Column()
    pr_merged_at = db.Column()
    pr_merge_commit_sha = db.Column()
    pr_teams = db.Column())
    pr_milestone = db.Column()
    pr_commits_url = db.Column()
    pr_review_comments_url = db.Column()
    pr_review_comment_url = db.Column()
    pr_comments_url = db.Column()
    pr_statuses_url = db.Column()
    pr_meta_head_id = db.Column()
    pr_meta_base_id = db.Column()
    pr_src_issue_url = db.Column()
    pr_src_comments_url = db.Column()
    pr_src_review_comments_url = db.Column()
    pr_src_commits_url = db.Column()
    pr_src_statuses_url = db.Column()
    pr_src_author_association = db.Column()
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())
    
class Pull_Requests(db.Model):
    __tablename__ = 'pull_requests'
    pull_request_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    repo_id = db.Column(db.BigInteger)
    pr_url = db.Column()
    pr_src_id = db.Column()
    pr_src_node_id = db.Column()
    pr_html_url = db.Column()
    pr_diff_url = db.Column()
    pr_patch_url = db.Column()
    pr_issue_url = db.Column()
    pr_augur_issue_id = db.Column()
    pr_src_number = db.Column()
    pr_src_state = db.Column()
    pr_src_locked = db.Column()
    pr_src_title = db.Column()
    pr_augur_contributor_id = db.Column()
    pr_body = db.Column()
    pr_created_at = db.Column()
    pr_updated_at = db.Column()
    pr_closed_at = db.Column()
    pr_merged_at = db.Column()
    pr_src_issue_url = db.Column()
    pr_src_comments_url = db.Column()
    pr_src_review_comments_url = db.Column()
    pr_src_commits_url = db.Column()
    pr_src_statuses_url = db.Column()
    pr_src_author_association = db.Column()
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())
        
        
class Commits(db.Model):
    __tablename__ = 'commits'
    cmt_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    repo_id = db.Column()
    cmt_commit_hash = db.Column()
    cmt_author_name = db.Column()
    cmt_author_raw_email = db.Column()
    cmt_author_affiliation = db.Column()
    cmt_committer_name = db.Column()
    cmt_committer_raw_email = db.Column()
    cmt_committer_email = db.Column()
    cmt_committer_date = db.Column()
    cmt_committer_affiliation = db.Column()
    cmt_added = db.Column()
    cmt_removed = db.Column()
    cmt_whitespace = db.Column()
    cmt_date_attempted = db.Column()
    cmt_ght_author_id = db.Column()
    cmt_author_platform_username = db.Column()
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())
        
class ContributorAliases(db.Model):
    __tablename__ = 'commits'
    cmt_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    cmt_commit_hash = db.Column()
    cmt_author_name = db.Column()
    cmt_author_raw_email = db.Column()
    cmt_author_affiliation = db.Column()
    cmt_committer_name = db.Column()
    cmt_author_platform_username = db.Column()
    tool_source = db.Column(db.String())
    tool_version = db.Column(db.String())
    data_source = db.Column(db.String())
    data_collection_date = db.Column(db.TIMESTAMP())
    """
